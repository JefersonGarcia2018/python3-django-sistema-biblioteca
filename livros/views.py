from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Autor
from .models import Livro
from .forms import LivroForm

@login_required #Decorator que verifica se o usuário está logado (Middleware)
def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros/lista.html', {'livros': livros})

@login_required #Decorator que verifica se o usuário está logado (Middleware)
def novo_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = LivroForm()
    return render(request, 'livros/form_livro.html', {'form': form})

@login_required #Decorator que verifica se o usuário está logado (Middleware)
def editar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        # O segredo está aqui: passamos o 'livro' recuperado para a 'instance'
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livros/form_livro.html', {'form': form, 'editando': True})

@login_required #Decorator que verifica se o usuário está logado (Middleware)
def excluir_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('lista_livros')
    return render(request, 'livros/confirmar_exclusao.html', {'livro': livro})

@login_required #Decorator que verifica se o usuário está logado (Middleware)
def cadastrar_autor_ajax(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        biografia = request.POST.get('biografia', '')
        if nome:
            if Autor.objects.filter(nome__iexact=nome).exists():
                return JsonResponse({'error': 'Já existe um autor cadastrado com este nome.'}, status=400)
                
            autor = Autor.objects.create(nome=nome, biografia=biografia)
            return JsonResponse({'id': autor.id, 'nome': autor.nome}, status=201)
    return JsonResponse({'error': 'Erro ao cadastrar autor'}, status=400)