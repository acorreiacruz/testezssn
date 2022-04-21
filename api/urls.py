from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    
    path(
        'sobreviventes/<int:id>/', 
        views.SobreviventeDetalharAPIView.as_view(), 
        name="detalhar_alterar_deletar_sobrevivente"
    ),
    path(
        'sobreviventes/', 
        views.SobreviventesListarAPIView.as_view(), 
        name="listar_postar_sobrevivente"
    ),
    path(
        'inventarios/<int:id>/',
        views.InventarioDetalharAPIView.as_view(),
        name="detalhar_alterar_deletar_inventario"
    ),
    path(
        'inventarios/', 
        views.InventarioLListarAPIVIew.as_view(), 
        name="inventarios"
    ),

]