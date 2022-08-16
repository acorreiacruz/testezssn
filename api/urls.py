from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter


app_name = "api"


api_sobreviventes_urls = SimpleRouter()
api_sobreviventes_urls.register(
    'sobreviventes',
    views.SobreviventeModelViewSet,
    basename='api-sobreviventes'
)


urlpatterns = [
    path(
        'sobreviventes/<int:pk>/denuncia/',
        views.denunciar_infectado,
        name='denunciar_infectado'
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

urlpatterns += api_sobreviventes_urls.urls