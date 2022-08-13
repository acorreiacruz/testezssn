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
    path(
        'sobreviventes/trocas/<int:id1>/<str:itm1>/<int:qnt1>/<int:id2>/<str:itm2>/<int:qnt2>/',
        views.NegociarItens().as_view(),
        name="negociar_itens"
    ),
    path(
        'sobreviventes/relatorio/infectados/',
        views.porcentagem_infectados,
        name='porcentagem_infectados'
    ),
    path(
        'sobreviventes/relatorio/nao-infectados/',
        views.porcentagem_nao_infectados,
        name='porcentagem_nao_infectados'
    ),
    path(
        'sobreviventes/relatorio/medias-dos-inventarios/',
        views.medias_dos_inventarios,
        name='medias_do_inventario'
    ),
]