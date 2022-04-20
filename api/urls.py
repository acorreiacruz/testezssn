from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path('sobreviventes/', views.get_sobreviventes, name="sobreviventes"),
    path('inventarios/', views.get_inventarios, name="inventarios"),
]