from django.urls import path
from .import views
from rest_framework.routers import SimpleRouter
from rest_framework.renderers import JSONRenderer


app_name = "api"


api_sobreviventes_urls = SimpleRouter()
api_sobreviventes_urls.register(
    'sobreviventes',
    views.SobreviventeModelViewSet,
    basename='api-sobreviventes'
)

urlpatterns = [
    path(
        'sobreviventes/trocas/<int:id1>/<str:itm1>/<int:qnt1>/<int:id2>/<str:itm2>/<int:qnt2>/',
        views.NegociarItens().as_view(),
        name="negociar_itens"
    ),
]

urlpatterns += api_sobreviventes_urls.urls