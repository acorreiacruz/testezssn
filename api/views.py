from webbrowser import get
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


class LocalAPIView(APIView):

    '''
        View que permite o sobrevivente tanto acessar sua localização bem como atualizá-la a partir do seu id.
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


class NegociarItens(APIView):
    '''
        Classe responsável por tratar de toda a parte de negociação de itens entre os sobreviventes.
    '''
    tabela_de_precos = {
            'agua':4,
            'alimentacao':3,
            'medicacao':2,
            'municao':1,
        }

    def get_sobrevivente(self, id):
        sobrevivente = get_object_or_404(
            Sobrevivente,
            pk=id
        )
        return sobrevivente

    def get_inventario(self, id):
        sobrevivente = self.get_sobrevivente(id)
        return sobrevivente.inventario

    def validar_troca(self, invt1, itm1, qnt1, invt2, itm2, qnt2):
        if qnt1 > getattr(invt1, itm1) or qnt2 > getattr(invt2, itm2):
            return False

        if qnt1 < 0 or qnt2 < 0:
            return False

        if (getattr(invt1, itm1) == 0 and qnt1 > 0) or (getattr(invt2, itm2) == 0 and qnt2 > 0):
            return False

        if self.tabela_de_precos[itm1] * qnt1 != self.tabela_de_precos[itm2] * qnt2:
            return False

        return True


    def negociar_itens(self, request, usr1, itm1, qnt1, usr2, itm2, qnt2):
        inventario1 = self.get_inventario(usr1)
        inventario2 = self.get_inventario(usr2)

        if self.validar_troca( inventario1, itm1, qnt1, inventario2, itm2, qnt2):

            valor_inicial = getattr(inventario1, itm1)
            setattr(inventario1, itm1, valor_inicial - qnt1)
            valor_inicial = getattr(inventario1, itm2)
            setattr(inventario1, itm2, valor_inicial + qnt2)

            valor_inicial = getattr(inventario2, itm2)
            setattr(inventario2, itm2, valor_inicial - qnt2)
            valor_inicial = getattr(inventario2, itm1)
            setattr(inventario2, itm1, valor_inicial + qnt1)

            inventario1.save()
            inventario2.save()

            return Response({
                "sucesso": "Operação de troca realizada com sucesso!"
            }, status.HTTP_202_ACCEPTED)

        return Response({
            "invalido": "Operação de troca inválida!"
        }, status.HTTP_403_FORBIDDEN)


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




