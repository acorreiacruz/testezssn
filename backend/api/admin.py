from django.contrib import admin
from .models import Inventario, Sobrevivente, Local


@admin.register(Sobrevivente)
class SobreviventeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'nome', 'idade', 'sexo', 'infectado',
        'denuncias', 'ultimo_local', 'inventario'
    )


@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'agua', 'alimentacao',
        'medicacao', 'municao'
    ]


@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'latitude', 'longitude',
    ]


