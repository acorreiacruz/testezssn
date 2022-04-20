from rest_framework import serializers

from .models import Inventario, Sobrevivente


class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = ('id','agua','alimentacao','medicacao','municao','sobrevivente')

class SobreviventeSerializer(serializers.ModelSerializer):

    inventario = InventarioSerializer()

    class Meta:
        model = Sobrevivente
        fields = ('id','nome','idade','sexo','infectado','inventario')


