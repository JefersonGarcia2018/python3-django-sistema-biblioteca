from django.db import models

#Criação do Model "Autor"
class Autor(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    biografia = models.TextField(blank=True)

    def __str__(self):
        return self.nome

#Criação do Model "Livro"
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='livros')
    isbn = models.CharField(max_length=13, unique=True)
    data_publicacao = models.DateField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo