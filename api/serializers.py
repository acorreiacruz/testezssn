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
            'id', 'nome', 'idade', 'sexo', 'infectado',
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

    def create(self, validated_data):
        # Verifica se os dados de último local foram enviados
        try:
            ultimo_local = validated_data.pop('ultimo_local')
        except Exception:
            ultimo_local = None
        else:
            ultimo_local = Local.objects.create(**ultimo_local)

        inventario = validated_data.pop('inventario')
        inventario = Inventario.objects.create(**inventario)
        sobrevivente = Sobrevivente.objects.create(
            ultimo_local=ultimo_local,
            inventario=inventario,
            **validated_data
        )

        return sobrevivente

    def update(self, instance, validated_data):
        ultimo_local = instance.ultimo_local
        ultimo_local.latitude = validated_data.get('latitude', ultimo_local.latitude)
        ultimo_local.longitude = validated_data.get('longitude', ultimo_local.longitude)
        instance.save()
        return instance