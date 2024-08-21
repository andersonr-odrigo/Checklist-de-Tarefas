from django.db import models


# Create your models here.
class Todo(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    data_criacao = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    data_entrega = models.DateTimeField(null=False, blank=False)
    data_finalizacao = models.DateTimeField(
        null=True,
    )
