from tabnanny import verbose
from django.db import models
from datetime import date
import usuario
from usuario.models import Usuario

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome 

class Livros(models.Model):
    nome = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 30)
    co_autor = models.CharField(max_length = 30, blank=True)
    data_cadastro = models.DateField(default= date.today)
    emprestado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    

    class Meta: # a classe meta dentro de uma classe faz com que seja possivel alterar o nome da classe para que a visualização do admin não fique com duas letras s no final
        verbose_name = 'Livro' 

    def __str__(self):
        return self.nome

class Emprestimos(models.Model):
    nome_emprestado = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, blank=True, null=True)
    nome_emprestado_anonimo = models.CharField(max_length=30, blank=True, null=True)
    data_emprestimo = models.DateField(blank=True, null=True)
    data_devolucao = models.DateField(blank=True, null=True)
    livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING)

    def __str__(self):
        if self.nome_emprestado:
            return f'{self.nome_emprestado} / {self.livro}'
        else:
            return f'{self.nome_emprestado_anonimo} / {self.livro}'


