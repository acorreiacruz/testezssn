from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Sobrevivente, Inventario
from .serializers import SobreviventeSerializer, InventarioSerializer
from rest_framework import status

@api_view(['GET'])
def home(request):
    return Response(data={'nome':'Antonio', 'idade':23, 'sexo':'masculino', 'infectado':False}, status=status.HTTP_404_NOT_FOUND)
