from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Sobrevivente, Inventario
from .serializers import SobreviventeSerializer, InventarioSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination

class PaginacaoCustomizada(PageNumberPagination):
    page_size = 2

class SobreviventeListCreateAPIView(ListCreateAPIView):
    queryset = Sobrevivente.objects.all()
    serializer_class = SobreviventeSerializer
    pagination_class = PaginacaoCustomizada


class SobreviventeRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Sobrevivente.objects.all()
    serializer_class = SobreviventeSerializer

class InventarioListCreateAPIView(ListCreateAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    pagination_class = PaginacaoCustomizada

class InventarioRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer




