from xmlrpc.client import Boolean
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Sobrevivente, Inventario
from .serializers import SobreviventeSerializer, InventarioSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view




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


# Definindo a View que ira lidar com toda a parte de negociações da API
class InvetarioNegociar(APIView):

    # Tabela de preços do inventário
    tabela_de_precos = {
        "agua": 4,
        "alimentacao": 3,
        "medicacao": 2,
        "municao": 3
    }


    def get_sobrevivente_pelo_id(self, id: int) -> Sobrevivente:
        '''
            Método que retorna uma instância da classe Sobrevivente pela primary key
        '''

        sobrevivente = get_object_or_404(
            Sobrevivente.objects.all(),
            id=id
        )
        
        return sobrevivente

    def get_inventario(self, sobrevivente: Sobrevivente) -> Inventario:
        '''
            Método que recebe uma isntância de Sobrevivente e retorna o inventario.
        '''
        return sobrevivente.inventario


    def se_infectado(self, id: int) -> Boolean:
        '''
            Método que verifica de se uma instância da classe Sobrevivente esta infectada a partir de sua primary key, retornando True para caso esteja infectado e False caso contrário.
        '''

        sobrevivente = self.get_sobrevivente_pelo_id(id)

        if sobrevivente.infectado:
            return True
        else:
            return False


    def realizar_negocio(self, inventario1: Inventario , inventario2: Inventario, item1: str, item2: str) -> None:
        '''
            Função que recebe dois objetos do tipo Sobrevivente, os itens que cada um quer trocar, e realiza a processo de negociacao de itens entre eles.
        '''

        pontos1 = self.tabela_de_precos[item1] * inventario1.item1
        pontos2 = self.tabela_de_precos[item2] * inventario2.item2

        if pontos1 == pontos2 :
            ...



    def get(self, request, id1: int, id2: int):

        sobrevivente1 = self.get_sobrevivente_pelo_id(id1)
        sobrevivente2 = self.get_sobrevivente_pelo_id(id2)
        
        if self.se_infectado(id1) and self.se_infectado(id2):
            return Response(
                data={"proibido":"Um ou ambos os sobreviventes infectados!"},
                status=status.HTTP_403_FORBIDDEN
            )

        inventario1 = self.get_inventario(sobrevivente1)
        inventario2 = self.get_inventario(sobrevivente2)

        self.realizar_negocio(inventario1, inventario2)

        return Response(
            data={"sucesso":"Negócio realizado com sucesso!"},
            status = status.HTTP_202_ACCEPTED
        )

@api_view(['GET'])
def denunciar_infectado(request, pk):
    '''
        View que ira lidar com as denúncias de infecção de um sombrevivente.
    '''
    sobrevivente = get_object_or_404(
        Sobrevivente.objects.all(),
        id=pk
    )

    sobrevivente.quant_denuncias += 1

    if sobrevivente.quant_denuncias == 3:
        sobrevivente.infectado = True
    
    sobrevivente.save()

    return Response(
        data={"sucesso":"Denúncia efetuada com sucesso!"},
        status=status.HTTP_201_CREATED
    )

    

    


    
