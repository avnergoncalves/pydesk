from django.db import models

# Create your models here.
class Enterprise(models.Model):
    rasao_social = models.CharField(max_length=200, blank=False)
    nome_fantasia = models.CharField(max_length=200, blank=False)
    cnpj = models.CharField(max_length=100, blank=True)
    inscricao_estadual = models.CharField(max_length=100, blank=True)
    endereco = models.CharField(max_length=100, blank=True)
    observacao = models.CharField(max_length=1024, blank=True)