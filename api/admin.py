from django.contrib import admin
from .models import Inventario, Sobrevivente


@admin.register(Sobrevivente)
class SobreviventeAdmin(admin.ModelAdmin):
    list_display = ('nome','idade','sexo','infectado')


@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('agua','alimentacao','medicacao','municao')
