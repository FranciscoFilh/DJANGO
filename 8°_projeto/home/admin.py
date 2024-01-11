from django.contrib import admin
from .models import Livro

class ListLivros(admin.ModelAdmin):
    list_display = ('nome_do_livro','ano_da_publicacao','quantidade_de_paginas','nome_do_autor','nome_da_editora','preco')

admin.site.register(Livro, ListLivros)
