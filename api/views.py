from xmlrpc.client import Boolean
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Sobrevivente, Inventario
from .serializers import SobreviventeSerializer, InventarioSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination

"""
    Infectado:
        - Não pode acessar/manipular o inventário
        - Não pode negociar
"""


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

# Definindo como path para a negociação /api/inventarios/id1/negociar/id2/
class InvetarioNegociacar(APIView):

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


    def se_infectado(self, id: int) -> Boolean:
        '''
            Método que verifica de se uma instância da classe Sobrevivente esta infectada a partir de sua primary key, retornando True para caso esteja infectado e False caso contrário.
        '''

        sobrevivente = self.get_sobrevivente_pelo_id(id)

        if sobrevivente.infectado:
            return True
        else:
            return False


    def realizar_negocio(self, sobrevivente1: Sobrevivente , sobrevivente2: Sobrevivente) -> None:
        '''
            Função que recebe dois os objetos do tipo inventário e realiza a processo de negociacao de itens entre eles. Limitando a troca de itens do inventário a no máximo dois itens.
        '''
        
        inventario1 = sobrevivente1.inventario
        inventario2 = sobrevivente2.inventario


    
    def get(self, request, id1: int, id2: int):

        sobrevivente1 = self.get_sobrevivente_pelo_id(id1)
        sobrevivente2 = self.get_sobrevivente_pelo_id(id2)
        
        if self.se_infectado(id1) and self.se_infectado(id2):
            return Response(
                data={"proibido":"Um ou ambos os sobreviventes infectados!"},
                status=status.HTTP_403_FORBIDDEN
            )

        self.realizar_negocio(sobrevivente1, sobrevivente2)

        return Response(
            data={"sucesso":"Negócio realizado com sucesso!"},
            status = status.HTTP_202_ACCEPTED
        )

