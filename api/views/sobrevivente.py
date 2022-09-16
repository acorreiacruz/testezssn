from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from ..permission import EhInfectado
from ..models import Sobrevivente
from ..serializers import SobreviventeSerializer
from rest_framework import viewsets
from ..pagination import PaginacaoCustomizada
from rest_framework.decorators import action


class SobreviventeModelViewSet(viewsets.ModelViewSet):
    queryset = Sobrevivente.objects.all()
    serializer_class = SobreviventeSerializer
    http_method_names = ['get','post','patch','delete','options']
    campos = ['nome','sexo','infectado','agua','alimentacao','medicacao','municao']
    permission_classes = [AllowAny, EhInfectado]

    def avaliar_partial(self):
        chaves = list(self.request.data.keys())
        for campo in self.campos:
            if campo in chaves:
                return False
        return True

    def partial_update(self, request, *args, **kwargs):
        sobrevivente = self.get_object()

        if not self.avaliar_partial():
            return Response(
                {"detail":"Só é permitido alterar a latitude e longitude do sobrevivente!"},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = self.get_serializer(
            instance=sobrevivente,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save(**request.data)

        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def denunciar(self, request, *args, **kwargs):
        sobrevivente = self.get_object()
        sobrevivente.denuncias += 1
        if sobrevivente.denuncias == 3:
            sobrevivente.infectado = True
        sobrevivente.save()
        return Response(status=status.HTTP_201_CREATED)