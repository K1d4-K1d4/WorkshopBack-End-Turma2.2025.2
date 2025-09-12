from django.db import models

class Endereco(models.Model):
   cep = models.CharField(max_length=9)
   logradouro = models.CharField(max_length=255)
   bairro = models.CharField(max_length=255)
   localidade = models.CharField(max_length=255)
   uf = models.CharField(max_length=2)
   
   def __str__(self):
      return (f"Cep: {self.cep}, Rua: {self.logradouro}, Bairro: {self.bairro}, Cidade: {self.localidade}, {self.uf}")
