from django.shortcuts import render
from django.http import HttpResponse
from .models import Carne

def home(request):
    minhas_carnes = Carne.objects.all()

    context = {
        'carnes': minhas_carnes,
    }

    return render(request,'home/index.html', context)