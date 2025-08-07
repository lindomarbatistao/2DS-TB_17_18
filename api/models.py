from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    data_nasc =  models.DateField(null=True, blank=True)
    nacion = models.CharField(max_length=30, null=True, blank=True)
    biogra = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

