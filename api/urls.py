from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path(
        'sobreviventes/<int:pk>/', 
        views.SobreviventeRetriveUpdateDestroyAPIView.as_view(), 
        name="detalhar_alterar_deletar_sobrevivente"
    ),
    path(
        'sobreviventes/', 
        views.SobreviventeListCreateAPIView.as_view(), 
        name="listar_postar_sobrevivente"
    ),
    path(
        'inventarios/<int:id1>/negociar/<int:id2>/',
        views.InvetarioNegociacar.as_view(),
        name="inventario_negociar"
    
    ),
    path(
        'inventarios/<int:pk>/',
        views.InventarioRetriveUpdateDestroyAPIView.as_view(),
        name="detalhar_alterar_deletar_inventario"
    ),
    path(
        'inventarios/', 
        views.InventarioListCreateAPIView.as_view(), 
        name="inventarios"
    ),
]