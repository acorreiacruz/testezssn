from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path(
        'sobreviventes/<int:id>/', 
        views.detalhar_alterar_e_deletar_sobrevivente, 
        name="detalhar_alterar_deletar_sobrevivente"
    ),
    path(
        'sobreviventes/', 
        views.listar_ou_postar_sobrevivente, 
        name="listar_postar_sobrevivente"
    ),
    path(
        'inventarios/<int:id>/',
        views.detalhar_alterar_e_deletar_inventario,
        name="detalhar_alterar_deletar_inventario"
    ),
    path(
        'inventarios/', 
        views.listar_ou_postar_inventario, 
        name="inventarios"
    ),

]