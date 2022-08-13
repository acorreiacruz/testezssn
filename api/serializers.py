from rest_framework import serializers
from .models import Sobrevivente


class SobreviventeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sobrevivente
        fields = (
            'id','nome','idade','sexo','infectado',
            'denuncias','latitude', 'longitude',
            'agua','alimentacao','medicacao','municao'
        )


