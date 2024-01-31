from django.shortcuts import render, redirect
from .models import Agenda
from django.contrib import messages
from .forms import AgendaForm

def index(request):
    agendas = Agenda.objects.all()
    return render(request, 'agendas/index.html', {'agendas': agendas})

def cadastro(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Agenda cadastrada com Sucesso!')
            form = AgendaForm()
        else:
            messages.error(request, 'Erro ao salva agenda!')
    else:
        form = AgendaForm()
    
    return render(request, 'agendas/cadastro.html', { 'form': form})

def deletar(request, id):
    deleteme = Agenda.objects.get(id=id)
    if request.method == 'POST':
        deleteme.delete()
        return redirect('/')
    return render(request, 'agendas/deletar.html')