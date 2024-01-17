from django.shortcuts import render
from .forms import ContatoForm, ProdutoModelForm
from django.contrib import messages


def index(request):
    return render(request, 'home/index.html')

def contato(request):
    form = ContatoForm(request.POST)

    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem enviada')
            print(f'Nome: {nome}')
            print(f'E-mail: {email}')
            print(f'Assunto: {assunto}')
            print(f'Mensagem: {mensagem}')

            messages.success(request, 'Mensagem enviada com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar seu e-mail')
        
    context = {
        'form': form
    }

    return render(request, 'home/contato.html', context)

def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto cadrastrado com sucesso.')
        else:
            messages.error(request, 'Falha no cadrastro do produto.')
    else:
        form = ProdutoModelForm()

    context = {
        'form': form
    }
                  
    return render(request, 'home/produto.html', context)