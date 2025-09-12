from django.db import models

#Para criar um modelo no banco de dados, criamos uma classe que vai ser o nome do objeto/banco(para gerenciamento)
#Com campos no estilo clássico de criação de tables em SQL
class Endereco(models.Model):
   cep = models.CharField(max_length=9)   
   logradouro = models.CharField(max_length=255)
   bairro = models.CharField(max_length=255)
   localidade = models.CharField(max_length=255)
   uf = models.CharField(max_length=2)
   #__str__ é um comando reservado para que a apresentação do modelo siga essas
   def __str__(self):
      return f"{self.cep} - {self.logradouro} - {self.bairro} - {self.localidade},{self.uf}"