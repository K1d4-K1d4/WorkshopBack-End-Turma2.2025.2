from django.db import models

class Endereco(models.Model):
    cep = models.CharField(max_length=9)  # Ex: "58035-000"
    logradouro = models.CharField(max_length=200)  # Ex: "Rua Presidente João Pessoa"
    bairro = models.CharField(max_length=100)  # Ex: "Centro"
    localidade = models.CharField(max_length=100)  # Ex: "João Pessoa"
    uf = models.CharField(max_length=2)  # Ex: "PB"
    

    def __str__(self):
        return f"{self.cep} - {self.logradouro}, {self.localidade}-{self.uf}"

