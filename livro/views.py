from django.shortcuts import render, redirect
from django.http import HttpResponse
import usuario 
from usuario.models import Usuario
from .models import Livros, Categoria, Emprestimos
from .forms import CadastroLivro

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        livros = Livros.objects.filter(usuario = usuario)
        form = CadastroLivro()
        return render(request, 'home.html', {'livros': livros, 
                                             'usuario_logado': request.session.get('usuario'),
                                             'form': form})
    else:
        return redirect('/auth/login/?status=2')

def ver_livros(request, id):
    if request.session.get('usuario'):
        livro = Livros.objects.get(id = id)
        categoria_livro = Categoria.objects.filter(usuario = request.session.get('usuario'))
        if request.session['usuario'] == livro.usuario.id:
            emprestimos = Emprestimos.objects.filter(livro = livro)
            form = CadastroLivro()
            return render(request, 'ver_livro.html', {'livro': livro, 
                                                      'categoria_livro': categoria_livro, 
                                                      'emprestimos': emprestimos, 
                                                      'usuario_logado': request.session.get('usuario'),
                                                      'form': form})
        else:
            return HttpResponse('esse livro não é seu')
    else:
        return redirect('/auth/login/?status=2')

def cadastrar_livro(request):
    if request.method == 'POST':
        form = CadastroLivro(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('livro salvo com sucesso')
        else:
            return HttpResponse('dados inválidos')

        

