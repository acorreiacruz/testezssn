from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Sobrevivente, Inventario
from .serializers import SobreviventeSerializer, InventarioSerializer
from rest_framework import status
from rest_framework.views import APIView


class SobreviventesListarAPIView(APIView):

    def get(self, request):
        sobreviventes = Sobrevivente.objects.all()
        serializer = SobreviventeSerializer(sobreviventes, many=True) 
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SobreviventeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) 
        serializer.save() 

class SobreviventeDetalharAPIView(APIView):

    def get_sobrevivente(self, id):
        sobrevivente = get_object_or_404(
            Sobrevivente.objects.all(),
            id=id
        )
        return sobrevivente

    def get(self, request, id):
        sobrevivente = self.get_sobrevivente(id)
        serializer = SobreviventeSerializer(sobrevivente)
        return Response(serializer.data)

    def put(self, request, id):
        sobrevivente = self.get_sobrevivente(id)
        serializer = SobreviventeSerializer(instance=sobrevivente, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        sobrevivente = self.get_sobrevivente(id)
        sobrevivente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class InventarioLListarAPIVIew(APIView):
    def get(self, request):
        inventarios = Inventario.objects.all()
        serializer = InventarioSerializer(inventarios, many=True)
        return Response(serializer.data)

    def post(self , request):
        serializer = InventarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class InventarioDetalharAPIView(APIView):
    
    def get_inventario(self, id):
        inventario = get_object_or_404(
            Inventario.objects.all(),
            id=id
        )
        return inventario

    def get(self, request, id):
        inventario = self.get_inventario(id)
        serializer = InventarioSerializer(inventario)
        return Response(serializer.data)        
    
    def put(self, request, id):
        inventario = self.get_inventario(id)
        serializer = InventarioSerializer(inventario, data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
    
    def delete(self, request, id):
        inventario = self.get_inventario(id)
        inventario.delete()
        return Response(status.HTTP_204_NO_CONTENT)       



