from django.db import models

# Create your models here.
# Todos esses fiels estão na documentação django# 


class Pacientes(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    rg = models.CharField(max_length=100, blank=True, null=True)
    data_nasc = models.DateTimeField(blank=True, null=True)
    endereco = models.CharField(max_length=80, blank=True, null=True)
    num_endereco = models.IntegerField(blank=True, null=True)
    bairro = models.CharField(max_length=60, blank=True, null=True)
    cep = models.CharField(max_length=100, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        managed = True
        db_table = 'pacientes'
    
    