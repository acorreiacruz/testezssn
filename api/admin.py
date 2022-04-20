from django.contrib import admin
from .models import Inventario, Sobrevivente


@admin.register(Sobrevivente)
class SobreviventeAdmin(admin.ModelAdmin):
    list_display = ('id','nome','idade','sexo','infectado')


@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('sobrevivente','agua','alimentacao','medicacao','municao')
