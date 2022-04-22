from django.contrib import admin
from .models import Inventario, Sobrevivente, Local


@admin.register(Sobrevivente)
class SobreviventeAdmin(admin.ModelAdmin):
    list_display = ('id','nome','idade','sexo','infectado','quant_denuncias')


@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('sobrevivente','agua','alimentacao','medicacao','municao')

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('latitude','longitude','sobrevivente')