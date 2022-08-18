from django.urls import path, include
from .import views
from .routers import api_sobreviventes_relatorios_urls, api_sobreviventes_urls


app_name = "api"


urlpatterns = [
    path(
            'sobreviventes/trocar/<int:id1>/<str:itm1>/<int:qnt1>/<int:id2>/<str:itm2>/<int:qnt2>/',
            views.NegociarAPIView.as_view(),
            name='api-sobreviventes-negociar-itens'
        ),
    path('', include(api_sobreviventes_urls.urls)),
    path('', include(api_sobreviventes_relatorios_urls.urls))
]
