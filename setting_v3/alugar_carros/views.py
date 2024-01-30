from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AlugarCarro
from .forms import AlugarCarroForm

def index(request):
    alugar_carros = AlugarCarro.objects.all
    return render(request,'alugar_carros/index.html', {'alugar_carros': alugar_carros})

def register(request):
    if request.method == 'POST':
        form = AlugarCarroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Carro adicionado com sucesso')
            form = AlugarCarroForm()
        else:
            messages.error(request, 'Erro ao adicionar carro')
    else:
        form = AlugarCarroForm()

    return render(request, 'alugar_carros/register.html', { 'form': form })

def delete_carro(request, id):
    alugar_carros = AlugarCarro.objects.get(id=id)
    if request.method == 'POST':
        alugar_carros.delete()
        return redirect('/')
    return render(request, 'alugar_carros/delete.html')