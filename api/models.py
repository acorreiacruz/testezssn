from django.db import models


class Inventario(models.Model):

    agua = models.PositiveIntegerField(null=False)
    alimentacao = models.PositiveIntegerField(null=False)
    medicacao = models.PositiveIntegerField(null=False)
    municao = models.PositiveIntegerField(null=False)

class Sobrevivente(models.Model):

    SEXO_CHOICES = (
        ('M','Masculino'),
        ('F','Feminino')
    )

    nome = models.CharField(null=False, blank=True, max_length=100)
    idade = models.PositiveIntegerField(null=False, blank=True,)
    sexo = models.CharField(choices= SEXO_CHOICES, null=False, blank=False,max_length=1)
    infectado = models.BooleanField()
    inventario = models.ForeignKey(Inventario,on_delete=models.CASCADE,null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nome
    
