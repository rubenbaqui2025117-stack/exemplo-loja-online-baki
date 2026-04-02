from django.db import models

class Vendedor(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    data_de_criacao = models.DateTimeField("Data de incrição")

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome

class Artigo(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    preco = models.CharField(max_length=200)
    data_de_criacao = models.DateTimeField("Data de publicação")
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
