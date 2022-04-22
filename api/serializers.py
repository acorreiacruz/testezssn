from rest_framework import serializers

from .models import Inventario, Sobrevivente, Local


class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ('latitude','longitude','sobrevivente')

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = ('id','agua','alimentacao','medicacao','municao','sobrevivente')

class SobreviventeSerializer(serializers.ModelSerializer):

    inventario = InventarioSerializer(many=False, read_only=True)
    local = LocalSerializer(many=False, read_only=True)

    class Meta:
        model = Sobrevivente
        fields = ('id','nome','idade','sexo','infectado','inventario','quant_denuncias','local')


