from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Sobrevivente, Inventario
from .serializers import SobreviventeSerializer, InventarioSerializer
from rest_framework import status


@api_view(['GET','POST'])
def get_sobreviventes(request):
    '''
        Lista todos os sobreviventes ou cria um novo
    '''
    if request.method == 'GET':
        sobreviventes = Sobrevivente.objects.all()
        serializer = SobreviventeSerializer(sobreviventes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SobreviventeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_inventarios(request):
    '''
        Lista todos os inventários
    '''
    if request.method == "GET":
        inventarios = Inventario.objects.all()
        serializer = InventarioSerializer(inventarios, many=True)
        return Response(serializer.data)
