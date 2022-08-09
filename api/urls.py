from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path(
        'sobreviventes/denuncias/<int:pk>/',
        views.denunciar_infectado,
        name='denunciar_infectado'
    ),
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
        'trocas/<int:id1>/<str:item1>/<int:qnt1>/<int:id2>/<str:item2>/<int:qnt2>/',
        views.InvetarioNegociar.as_view(),
        name="negociar_itens"

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
    path(
        'sobreviventes/local/<int:id>/',
        views.LocalAPIView.as_view(),
        name='detalhar_atualizar_local'
    )
]