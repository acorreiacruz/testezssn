from rest_framework import serializers
from .models import Sobrevivente, Inventario

class SobreviventeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sobrevivente
        fields = ('nome','idade','sexo','')

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = ('agua','alimentacao','medicacao','municao')