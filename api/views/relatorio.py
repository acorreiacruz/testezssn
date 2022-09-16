from ..serializers import SobreviventeSerializer
from rest_framework.response import Response
from ..models import Sobrevivente
from rest_framework import viewsets
from rest_framework.decorators import action
from django.db.models import Avg


class RelatorioViewSet(viewsets.GenericViewSet):

    queryset = Sobrevivente.objects.all()
    serializer_class = SobreviventeSerializer
    http_method_names = ['get']

    def get_queryset_qnt_objects(self):
        return self.get_queryset().count()

    def get_qnt_infectados_ou_nao(self, flag=True):
        return self.get_queryset().filter(infectado=flag).count()


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
            agua=Avg('inventario__agua'),
            alimentacao=Avg('inventario__alimentacao'),
            medicacao=Avg('inventario__medicacao'),
            municao=Avg('inventario__municao')
        )

        return Response(
            {
                "medias_dos_inventarios": {
                    'agua': f"{medias.get('agua'):.2f}",
                    'alimentacao': f"{medias.get('alimentacao'):.2f}",
                    'medicacao': f"{medias.get('medicacao'):.2f}",
                    'municao': f"{medias.get('municao'):.2f}"
                }
            }
        )
