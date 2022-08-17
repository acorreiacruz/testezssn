from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from .models import Sobrevivente
from .serializers import SobreviventeSerializer
from rest_framework import viewsets
from rest_framework import views
from .pagination import PaginacaoCustomizada
from rest_framework.decorators import action
from django.db.models import Sum, Avg


class SobreviventeModelViewSet(viewsets.ModelViewSet):
    queryset = Sobrevivente.objects.all()
    serializer_class = SobreviventeSerializer
    pagination_class = PaginacaoCustomizada
    http_method_names = ['get','post','patch','delete','options']
    campos = ['nome','sexo','infectado','agua','alimentacao','medicacao','municao']


    def get_queryset_qnt_objects(self):
        return self.get_queryset().count()

    def get_qnt_infectados_ou_nao(self, flag=True):
        return self.get_queryset().filter(infectado=flag).count()

    def avaliar_partial(self):
        chaves = list(self.request.data.keys())
        for campo in self.campos:
            if campo in chaves:
                return False
        return True

    def partial_update(self, request, *args, **kwargs):
        sobrevivente = self.get_object()

        if not self.avaliar_partial():
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(
            instance=sobrevivente,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def denunciar(self, request, *args, **kwargs):
        sobrevivente = self.get_object()
        sobrevivente.denuncias += 1
        if sobrevivente.denuncias == 3:
            sobrevivente.infectado = True
        sobrevivente.save()
        return Response(status=status.HTTP_201_CREATED)

    @action(
        methods=['get'], detail=False, url_name='relatorio-infectados',
        url_path='relatorio/infectados'
    )
    def porcentagem_infectados(self, request, *args, **kwargs):
        total = self.get_queryset_qnt_objects()
        infectados = self.get_qnt_infectados_ou_nao()
        return Response(
            {
                "infectados":f"{((infectados/total)*100):.2f} %"
            }
        )

    @action(
        methods=['get'], detail=False, url_name='relatorio-nao-infectados',
        url_path='relatorio/nao-infectados'
    )
    def porecentagem_nao_infectados(self, request, *args, **kwargs):
        total = self.get_queryset_qnt_objects()
        nao_infectados = self.get_qnt_infectados_ou_nao(False)
        return Response(
            {
                "nao infectados":f"{((nao_infectados/total)*100):.2f} %"
            }
        )

    @action(
        methods=['get'],
        url_path='relatorio/medias-dos-inventarios',
        detail=False,
        url_name='relatorio-medias-dos-inventarios'
    )
    def medias_dos_inventarios(self, request ,*args, **kwargs):

        medias = self.get_queryset().filter(infectado=False).aggregate(
            agua=Avg('agua'),
            alimentacao=Avg('alimentacao'),
            medicacao=Avg('medicacao'),
            municao=Avg('municao')
        )

        return Response(
            {
                "medias entre sobreviventes": {
                    'agua': f"{medias.get('agua'):.2f}",
                    'alimentacao': f"{medias.get('alimentacao'):.2f}",
                    'medicacao': f"{medias.get('medicacao'):.2f}",
                    'municao': f"{medias.get('municao'):.2f}"
                }
            }
        )

class NegociarItens(views.APIView):
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


