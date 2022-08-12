from django.db import models


class Sobrevivente(models.Model):

    SEXO_CHOICES = (
        ('M','Masculino'),
        ('F','Feminino')
    )

    nome = models.CharField(null=False, blank=True, max_length=100)
    idade = models.PositiveIntegerField(null=False, blank=True,)
    sexo = models.CharField(choices= SEXO_CHOICES, null=False, blank=False,max_length=1)
    infectado = models.BooleanField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    denuncias = models.PositiveIntegerField(null=False, blank=False, default=0)

    def __str__(self) -> str:
        return self.nome

class Local(models.Model):

    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
    sobrevivente = models.OneToOneField(Sobrevivente,on_delete=models.CASCADE, null=False)

class Inventario(models.Model):

    agua = models.PositiveIntegerField(null=False, default=0)
    alimentacao = models.PositiveIntegerField(null=False, default=0)
    medicacao = models.PositiveIntegerField(null=False, default=0)
    municao = models.PositiveIntegerField(null=False, default=0)
    sobrevivente = models.OneToOneField(Sobrevivente, on_delete=models.CASCADE, null=False)