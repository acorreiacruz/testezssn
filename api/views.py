from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Sobrevivente, Inventario
from .serializers import SobreviventeSerializer, InventarioSerializer
from rest_framework import status


@api_view(['GET','POST'])
def listar_ou_postar_sobrevivente(request):

    '''
        Lista todos os sobreviventes ou criar um novo
    '''

    if request.method == 'GET':
        sobreviventes = Sobrevivente.objects.all()
        serializer = SobreviventeSerializer(sobreviventes, many=True) 
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = SobreviventeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) 
        serializer.save() 


@api_view(['GET','PUT','DELETE'])
def detalhar_alterar_e_deletar_sobrevivente(request,id):
    '''
        Detalhar, alterar e deletar um sobrevivente
    '''
    try:
        sobrevivente = Sobrevivente.objects.get(id=id)
    except Sobrevivente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SobreviventeSerializer(sobrevivente)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = SobreviventeSerializer(sobrevivente, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    if request.method == 'DELETE':
        sobrevivente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def listar_ou_postar_inventario(request):

    '''
        Listar todos os inventários ou criar um novo
    '''

    if request.method == "GET":
        inventarios = Inventario.objects.all()
        serializer = InventarioSerializer(inventarios, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = InventarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)



@api_view(['GET','PUT','DELETE'])
def detalhar_alterar_e_deletar_inventario(request,id):

    '''
        Detalhar, alterar e deletar um inventário
    '''

    try:
        inventario = Inventario.objects.get(id=id)
    except Inventario.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InventarioSerializer(inventario)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = InventarioSerializer(inventario, data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
    
    if request.method == 'DELETE':
        inventario.delete()
        return Response(status.HTTP_204_NO_CONTENT)

