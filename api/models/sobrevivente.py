from django.db import models
from .inventario import Inventario
from .local import Local


class Sobrevivente(models.Model):

    SEXO_CHOICES = (
        ('M','Masculino'),
        ('F','Feminino')
    )

    nome = models.CharField(null=False, blank=True, max_length=100)
    idade = models.PositiveIntegerField(null=False, blank=True,)
    sexo = models.CharField(choices=SEXO_CHOICES, null=False, blank=False, max_length=1)
    infectado = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    denuncias = models.PositiveIntegerField(null=False, blank=False, default=0)
    inventario = models.OneToOneField(Inventario, on_delete=models.CASCADE)
    ultimo_local = models.OneToOneField(Local, on_delete=models.CASCADE, null=True)


    def __str__(self) -> str:
        return self.nome