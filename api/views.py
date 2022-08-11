from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Inventario, Local, Sobrevivente
from .serializers import (InventarioSerializer, LocalSerializer,
                          SobreviventeSerializer)


class PaginacaoCustomizada(PageNumberPagination):
    page_size = 2


class SobreviventeListCreateAPIView(ListCreateAPIView):
    queryset = Sobrevivente.objects.all()
    serializer_class = SobreviventeSerializer
    pagination_class = PaginacaoCustomizada


class SobreviventeRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Sobrevivente.objects.all()
    serializer_class = SobreviventeSerializer


class InventarioListCreateAPIView(ListCreateAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    pagination_class = PaginacaoCustomizada


class InventarioRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer


@api_view(['GET'])
def denunciar_infectado(request, pk):
    '''
        View que ira lidar com as denúncias de infecção de um sobrevivente.
    '''
    sobrevivente = get_object_or_404(
        Sobrevivente.objects.all(),
        id=pk
    )

    sobrevivente.denuncias += 1

    if sobrevivente.denuncias == 3:
        sobrevivente.infectado = True

    sobrevivente.save()

    return Response(
        data={"sucesso":"Denúncia efetuada com sucesso!"},
        status=status.HTTP_201_CREATED
    )


class LocalAPIView(APIView):

    '''
        View que permite o sobrevivente tanto acessar sua localização bem como atualizar a partir do id.
    '''

    def get_local(self, id):
        local = get_object_or_404(
            Local,
            sobrevivente = id
        )
        return local

    def get(self, request, id):
        local = self.get_local(id)
        serializer = LocalSerializer(local)
        return Response(data=serializer.data)

    def post(self, request, id):
        local = self.get_local(id)
        serializer = LocalSerializer(instance=local, data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data)


# Definindo a View que ira lidar com toda a parte de negociações da API
class InvetarioNegociar(APIView):

    # Tabela de preços do inventário
    tabela_de_precos = {
        "agua": 4,
        "alimentacao": 3,
        "medicacao": 2,
        "municao": 3
    }

    def get_sobrevivente_pelo_id(self, id):
        '''
            Método que retorna uma instância da classe Sobrevivente pela primary key
        '''

        sobrevivente = get_object_or_404(
            Sobrevivente.objects.all(),
            id=id
        )

        return sobrevivente

    def get_inventario(self, sobrevivente):
        '''
            Método que recebe uma isntância de Sobrevivente e retorna o inventario.
        '''
        return sobrevivente.inventario


    def se_infectado(self, id):
        '''
            Método que verifica de se uma instância da classe Sobrevivente esta infectada a partir de sua primary key, retornando True para caso esteja infectado e False caso contrário.
        '''

        sobrevivente = self.get_sobrevivente_pelo_id(id)

        return True if sobrevivente.infectado else False


    def realizar_negocio(self, inventario1, inventario2, item1, item2, quant1, quant2):
        '''
            Função que recebe dois objetos do tipo Sobrevivente, os itens que cada um quer trocar, e realiza a processo de negociacao de itens entre eles.

        '''

        # Item1 : é o item que sobrevivente1 dono do inventário1 quer negociar
        # Quant1: é quantidade do item1 que o sobrevivente1 quer negociar
        # Item2: é o item que o sobrevivente2 dono do invntário2 quer negociar
        # Quant2: é quantidade do item2 que o sobrevivente2 quer negociar

        if quant1 < inventario1.item1 and quant2 < inventario2.item2:
            pontos1 = self.tabela_de_precos[item1] * quant1
            pontos2 = self.tabela_de_precos[item2] * quant2
            if pontos1 == pontos2:
                inventario1.item1 -= quant1
                inventario1.item2 += quant2
                inventario2.item2 -= quant2
                inventario2.item1 += quant1
                inventario1.save()
                inventario2.save()

                return Response(
                    data={"sucesso":"Negociação realizada com sucesso!"},
                    status=status.HTTP_202_ACCEPTED
                )

            return Response(
                data={"invalido":"Negociaçao não igualitaária!"},
                status=status.HTTP_406_NOT_ACCEPTABLE
            )

        return Response(
            data={"invalido":"Negociaçao não igualitaária!"},
            status=status.HTTP_406_NOT_ACCEPTABLE
        )


    def get(self, request, id1, id2, item1, item2 , quant1, quant2):

        sobrevivente1 = self.get_sobrevivente_pelo_id(id1)
        sobrevivente2 = self.get_sobrevivente_pelo_id(id2)

        if self.se_infectado(id1) and self.se_infectado(id2):
            return Response(
                data={"proibido":"Um ou ambos os sobreviventes infectados!"},
                status=status.HTTP_403_FORBIDDEN
            )

        inventario1 = self.get_inventario(sobrevivente1)
        inventario2 = self.get_inventario(sobrevivente2)

        self.realizar_negocio(inventario1, inventario2, item1, item2 , quant1, quant2)

        return Response(
            data={"sucesso":"Negócio realizado com sucesso!"},
            status = status.HTTP_202_ACCEPTED
        )






