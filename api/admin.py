from django.contrib import admin
from .models import Inventario, Sobrevivente, Local


@admin.register(Sobrevivente)
class SobreviventeAdmin(admin.ModelAdmin):
    list_display = (
        'id','nome','idade','sexo','infectado',
        'denuncias','latitude', 'longitudade',
        'agua','alimentacao','medicacao','municao'
    )
