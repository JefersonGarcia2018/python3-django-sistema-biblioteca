from django.contrib.auth.models import AbstractUser
from django.db import models

#Criação do Model de Usuário customizado, herdando do AbstractUser
class Usuario(AbstractUser):
    # Adicione campos extras aqui no futuro, se precisar
    pass
