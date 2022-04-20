from rest_framework import serializers

from .models import Inventario, Sobrevivente


class SobreviventeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sobrevivente
        fields = ('id','nome','idade','sexo','infectado')

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = ('id','agua','alimentacao','medicacao','municao','sobrevivente')
