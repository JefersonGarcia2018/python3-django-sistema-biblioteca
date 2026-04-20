from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UsuarioCreationForm
from django.contrib import messages

def cadastro(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')  # Faz o login automaticamente após registro
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('lista_livros')
    else:
        form = UsuarioCreationForm()
    
    return render(request, 'usuarios/cadastro.html', {'form': form})
