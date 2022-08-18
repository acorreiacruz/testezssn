from django.db import models


class Inventario(models.Model):
    agua = models.PositiveIntegerField(null=False, blank=False, default=0)
    alimentacao = models.PositiveIntegerField(null=False, blank=False, default=0)
    medicacao = models.PositiveIntegerField(null=False, blank=False, default=0)
    municao = models.PositiveIntegerField(null=False, blank=False, default=0)