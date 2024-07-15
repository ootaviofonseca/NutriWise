from django.shortcuts import render, redirect

from apps.usuarios.forms import CadastroFormsAdm, CadastroFormsPa, LoginFormsAdm, LoginFormsPa

from django.contrib.auth.models import User

from django.contrib import auth

from django.contrib import messages

def loginAdm(request):
    form = LoginFormsAdm()

    if request.method == 'POST':
        form = LoginFormsAdm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            senha = form.cleaned_data['senha']

            user = auth.authenticate(username=username, password=senha)
            #verifica se o usuário existe no banco de dados e se a senha está correta
            
            if user is not None:
                auth.login(request, user)
                return redirect('index')
           
            else:
                messages.error(request, 'Usuário ou senha inválidos')
    
    return render(request, 'usuarios/loginAdm.html', {'form': form})

def loginPa(request):
    form = LoginFormsPa()

    if request.method == 'POST':
        form = LoginFormsPa(request.POST)
        
        if form.is_valid():
            cpf = form.cleaned_data['cpf']
            senha = form.cleaned_data['senha']

            user = auth.authenticate(username=cpf, password=senha)
            #verifica se o usuário existe no banco de dados e se a senha está correta
            
            if user is not None:
                auth.login(request, user)
                return redirect('index')
           
            else:
                messages.error(request, 'Usuário ou senha inválidos')
    
    return render(request, 'usuarios/loginPaciente.html', {'form': form})

def cadastroAdm(request):
    form = CadastroFormsAdm()

    if request.method == 'POST':
        form = CadastroFormsAdm(request.POST)
        
        if form.is_valid():
            
            #pega os dados do formulário
            username = form.cleaned_data['nomeCadastro']
            senha = form.cleaned_data['senhaCadastro']

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Nome de usuário já existe')
            else:
                user = User.objects.create_user(username=username, password=senha)
                user.save()
                messages.success(request, 'Cadastro realizado com sucesso')
                return redirect('loginAdm')
    
    return render(request, 'usuarios/cadastroAdm.html', {'form': form})

def cadastroPa(request):
    form = CadastroFormsPa()

    if request.method == 'POST':
        form = CadastroFormsPa(request.POST)
        
        if form.is_valid():
            #pega os dados do formulário
            username = form.cleaned_data['nomeCadastro']
            cpf = form.cleaned_data['cpfCadastro']
            senha = form.cleaned_data['senhaCadastro']

            if User.objects.filter(cpf=cpf).exists():
                messages.error(request, 'CPF já cadastrado')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Nome de usuário já existe')
            else:
                user = User.objects.create_user(username=username,id = cpf,  password=senha)
                user.save()
                messages.success(request, 'Cadastro realizado com sucesso')
                return redirect('loginPa')
    
    return render(request, 'usuarios/cadastroPaciente.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Deslogado com sucesso!')
    return redirect('login')