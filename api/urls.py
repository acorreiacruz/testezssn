from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path(
        'sobreviventes/<int:pk>/denuncia/',
        views.denunciar_infectado,
        name='denunciar_infectado'
    ),
    path(
        'sobreviventes/<int:pk>/',
        views.SobreviventeModelViewSet.as_view(
            {
                'get': 'retrieve',
                'patch': 'partial_update',
                'delete': 'destroy'
            }
        ),
        name='sobrevivente_buscar_alterar_excluir'
    ),
    path(
        'sobreviventes/',
        views.SobreviventeModelViewSet.as_view(
            {
                'get': 'list',
                'post': 'create'
            }
        ),
        name="sobrevivente_listar_criar"
    ),
]