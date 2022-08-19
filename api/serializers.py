from dataclasses import fields
from rest_framework import serializers
from .models import Sobrevivente, Inventario, Local


class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ['id', 'latitude', 'longitude']


class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = ['id', 'agua', 'alimentacao', 'medicacao', 'municao']



class SobreviventeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sobrevivente
        fields = (
            'id','nome','idade','sexo','infectado',
            'denuncias', 'ultimo_local', 'inventario'
        )

    ultimo_local = LocalSerializer(
        required=False,
        many=False,
        read_only=False
    )

    inventario = InventarioSerializer(
        required=True,
        many=False,
        read_only=False
    )


