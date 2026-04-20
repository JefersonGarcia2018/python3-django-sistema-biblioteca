from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_livros, name='lista_livros'),
    path('novo/', views.novo_livro, name='novo_livro'),
    path('editar/<int:pk>/', views.editar_livro, name='editar_livro'),
    path('excluir/<int:pk>/', views.excluir_livro, name='excluir_livro'),
    path('autor/novo/ajax/', views.cadastrar_autor_ajax, name='cadastrar_autor_ajax'),
]