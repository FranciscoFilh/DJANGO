from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Reuniao
from .forms import ReuniaoForm

def index(request):
    reunioes = Reuniao.objects.all
    return render(request,'reunioes/index.html', {'reunioes': reunioes})

def register(request):
    if request.method == 'POST':
        form = ReuniaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova reunião adicionada com sucesso')
            form = ReuniaoForm()
        else:
            messages.error(request, 'Erro ao adicionar nova reunião')
    else:
        form = ReuniaoForm()

    return render(request, 'reunioes/register.html', { 'form': form })

def delete_reuniao(request, id):
    comida_consumida = Reuniao.objects.get(id=id)
    if request.method == 'POST':
        comida_consumida.delete()
        return redirect('/')
    return render(request, 'reunioes/delete.html')