from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from ..models import Sobrevivente
from rest_framework import views


class NegociarAPIView(views.APIView):

    http_method_names = ['get']
    tabela_de_precos = {'agua': 5,'alimentacao': 4,'medicacao': 3,'municao': 2}


    def get_sobrevivente(self, id):
        sobrevivente = get_object_or_404(
            Sobrevivente,
            pk=id
        )
        return sobrevivente

    def se_infectado(self, sobrevivente):
        return True if sobrevivente.infectado else False

    def validar_troca(
        self, invent1, itm1, qnt1, invent2, itm2, qnt2
    ):
        if qnt1 > getattr(invent1, itm1) or qnt2 > getattr(invent2, itm2):
            return False

        if qnt1 < 0 or qnt2 < 0:
            return False

        if (getattr(invent1, itm1) == 0 and qnt1 > 0) or (getattr(invent2, itm2) == 0 and qnt2 > 0):
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
                    "detail": "Infectados nao podem realizar trocas!"
                },
                status.HTTP_403_FORBIDDEN
            )

        if self.validar_troca(
            sobrvt1.inventario,
            itm1,
            qnt1,
            sobrvt2.inventario,
            itm2,
            qnt2
        ):

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

            return Response(status.HTTP_202_ACCEPTED)

        return Response(
            data={
                "detail": "Operação de troca inválida!"
            },
            status=status.HTTP_403_FORBIDDEN
        )