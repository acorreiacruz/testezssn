from django.db import models


class Inventario(models.Model):
    agua = models.PositiveIntegerField(null=False, default=0)
    alimentacao = models.PositiveIntegerField(null=False, default=0)
    medicacao = models.PositiveIntegerField(null=False, default=0)
    municao = models.PositiveIntegerField(null=False, default=0)


class Local(models.Model):
    latitude = models.DecimalField(max_digits=22, decimal_places=16, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, null=True)


class Sobrevivente(models.Model):

    SEXO_CHOICES = (("M", "Masculino"), ("F", "Feminino"))

    nome = models.CharField(null=False, blank=False, max_length=100)
    idade = models.PositiveIntegerField(null=False, blank=False)
    sexo = models.CharField(choices=SEXO_CHOICES, null=False, blank=False, max_length=1)
    infectado = models.BooleanField(null=False, blank=False, default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    denuncias = models.PositiveIntegerField(null=False, blank=False, default=0)
    ultimo_local = models.OneToOneField(Local, on_delete=models.CASCADE, null=True)
    inventario = models.OneToOneField(Inventario, on_delete=models.CASCADE, null=False)

    def __str__(self) -> str:
        return self.nome
