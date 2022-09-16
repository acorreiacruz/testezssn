from rest_framework.routers import SimpleRouter
from . import views

api_sobreviventes_urls = SimpleRouter()
api_sobreviventes_urls.register(
    'sobreviventes',
    views.SobreviventeModelViewSet,
    basename='api-sobreviventes'
)

api_sobreviventes_relatorios_urls = SimpleRouter()
api_sobreviventes_relatorios_urls.register(
    'sobreviventes',
    views.RelatorioViewSet,
    basename='api-sobreviventes'
)