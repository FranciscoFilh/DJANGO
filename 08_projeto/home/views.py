from django.shortcuts import render
from django.http import HttpResponse
from .models import Livro

def home(request):
    meus_livros = Livro.objects.all()

    context = {
        'livros': meus_livros,
    }

    return render(request, 'home/index.html', context)