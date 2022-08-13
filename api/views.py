from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Sobrevivente
from .serializers import SobreviventeSerializer
from rest_framework import viewsets


class PaginacaoCustomizada(PageNumberPagination):
    page_size = 2


class SobreviventeModelViewSet(viewsets.ModelViewSet):
    queryset = Sobrevivente.objects.filter(infectado=False)
    serializer_class = SobreviventeSerializer
    pagination_class = PaginacaoCustomizada
    http_method_names = ['get','post','patch','delete','options']
    campos = ['nome','sexo','infectado','agua','alimentacao','medicacao','municao']

    def avaliar_partial(self, request_data):
        chaves = list(request_data.keys())
        for campo in self.campos:
            if campo in chaves:
                return False
        return True

    def partial_update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        sobrevivente = self.get_queryset().filter(pk=pk).first()
        if not self.avaliar_partial(request.data):
            return Response(
                {
                    "proibido":"Para alterar o campo infectado e os que formam o inventário, realize uma denúncia, negocie itens respectivamente. Os demais não podem ser alterados após a criação."
                },
                status.HTTP_403_FORBIDDEN
            )
        serializer = self.get_serializer(
            instance=sobrevivente,
            data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class NegociarItens(APIView):
    '''
        Classe responsável por tratar de toda a parte de negociação de itens entre os sobreviventes. A negociação ocorre de tal forma a permitir apenas um item de cada sobrevivente por transação.
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

    def se_infectado(self, sobrevivente):
        return True if sobrevivente.infectado else False

    def validar_troca(
        self, sobrvt1, itm1, qnt1, sobrvt2, itm2, qnt2
    ):
        if qnt1 > getattr(sobrvt1, itm1) or qnt2 > getattr(sobrvt2, itm2):
            return False

        if qnt1 < 0 or qnt2 < 0:
            return False

        if (getattr(sobrvt1, itm1) == 0 and qnt1 > 0) or (getattr(sobrvt2, itm2) == 0 and qnt2 > 0):
            return False

        if self.tabela_de_precos[itm1] * qnt1 != self.tabela_de_precos[itm2] * qnt2:
            return False

        return True


    def get(self, request, id1, itm1, qnt1, id2, itm2, qnt2):
        sobrvt1 = self.get_sobrevivente(id1)
        sobrvt2 = self.get_sobrevivente(id2)

        if self.se_infectado(sobrvt1) or self.se_infectado(sobrvt2):
            return Response(
                {
                    "proibido": "Infectados nao podem realizar trocas!"
                },
                status.HTTP_403_FORBIDDEN
            )

        if self.validar_troca( sobrvt1, itm1, qnt1, sobrvt2, itm2, qnt2):

            valor_inicial = getattr(sobrvt1, itm1)
            setattr(sobrvt1, itm1, valor_inicial - qnt1)
            valor_inicial = getattr(sobrvt1, itm2)
            setattr(sobrvt1, itm2, valor_inicial + qnt2)

            valor_inicial = getattr(sobrvt2, itm2)
            setattr(sobrvt2, itm2, valor_inicial - qnt2)
            valor_inicial = getattr(sobrvt2, itm1)
            setattr(sobrvt2, itm1, valor_inicial + qnt1)

            sobrvt1.save()
            sobrvt2.save()

            return Response({
                "sucesso": "Operacao de troca realizada com sucesso!"
            }, status.HTTP_202_ACCEPTED)

        return Response({
            "proibido": "Operacao de troca invalida!"
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
        data={"sucesso":"Denuncia efetuada com sucesso!"},
        status=status.HTTP_201_CREATED
    )

def numero_de_registros():
    total = len(Sobrevivente.objects.all())
    return total

def numero_de_infectados_ou_nao_infectados(flag):
   total =  len(Sobrevivente.objects.filter(infectado=flag))
   return total

@api_view(['get'])
def porcentagem_infectados(request):
    '''
        View responsavel por calcular a porcentagem de sobreviventes infectados.
    '''
    total = numero_de_registros()
    infectados = numero_de_infectados_ou_nao_infectados(True)
    return Response(
        {
            "Procentagem de Infectados":f"{((infectados/total)*100):.2f} %"
        }
    )


@api_view(['get'])
def porcentagem_nao_infectados(request):
    '''
        View responsável por calcular a porcentagem de sobreviventes nao infectados.
    '''
    total = numero_de_registros()
    nao_infectados = numero_de_infectados_ou_nao_infectados(False)
    return Response(
        {
            "Porcentagem de Nao Infectados":f"{((nao_infectados/total)*100):.2f} %"
        }
    )

@api_view(['get'])
def medias_dos_inventarios(request):
    '''
        View responsável por calcular a quantidade média de cada tipo de recurso por sobrevivente.
    '''
    total = numero_de_registros()
    query_set = Sobrevivente.objects.all()

    agua = 0,
    alimentacao = 0
    medicacao = 0
    municao = 0

    for sobrevivente in query_set:
        agua += sobrevivente.agua
        alimentacao += sobrevivente.alimentacao
        medicacao += sobrevivente.medicacao
        municao += sobrevivente.municao
    return Response(
        {
            "Medias Por Sobrevivente": {
                'agua': f'{agua/total:.2f}',
                'alimentacao': f'{alimentacao/total:.2f}',
                'medicacao': f'{medicacao/total:.2f}',
                'municao': f'{municao/total:.2f}'
            }
        }
    )

