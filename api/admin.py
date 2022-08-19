from django.contrib import admin
from .models import Sobrevivente


@admin.register(Sobrevivente)
class SobreviventeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'nome', 'idade', 'sexo', 'infectado',
        'denuncias', 'ultimo_local', 'inventario'
    )


