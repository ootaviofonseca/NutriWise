from django.shortcuts import get_object_or_404, render, redirect

from apps.galeria.models import TabelaNutricional
from apps.usuarios.forms import CadastroFormsNutricionista, CadastroFormsPa, LoginForms

from django.contrib.auth.models import User, Group

from django.contrib import auth

from django.contrib import messages

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)
        
        if form.is_valid():
            nome = form.cleaned_data['username']
            senha = form.cleaned_data['senha']

            user = auth.authenticate(username=nome, password=senha)
            #verifica se o usuário existe no banco de dados e se a senha está correta
            
            if user is not None:
                auth.login(request, user)
                
                # Verifica o grupo do usuário
                if user.groups.filter(name='nutricionista').exists():
                    # Redireciona para tela de nutricionista
                    messages.success(request, f"{nome} logado como nutricionista.")
                    return redirect('index')
                elif user.groups.filter(name='paciente').exists():
                    # Redireciona para tela de paciente
                    messages.success(request, f"{nome} logado como paciente.")
                    return redirect('index')
           
            else:
                messages.error(request, 'Usuário ou senha inválidos')
    
    return render(request, 'usuarios/login.html', {'form': form})

def pagina_inicial(request):
    usuario = get_object_or_404(User, id=request.user.id)
    tabela = TabelaNutricional.objects.filter(usuarioReferencia=usuario).first()
    
    context = {
        'usuario': usuario,
        'tabela': tabela,
    }
    return render(request, 'pagina_inicial.html', context)

def cadastroNutricionista(request):
    form = CadastroFormsNutricionista()

    if request.method == 'POST':
        form = CadastroFormsNutricionista(request.POST)
        
        if form.is_valid():
            
            
            #pega os dados do formulário
            nome = form.cleaned_data['nomeCadastro']
            email = form.cleaned_data['emailCadastro']
            senha = form.cleaned_data['senhaCadastro']

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Nome de usuário já existe')
            else:
                user = User.objects.create_superuser(
                    username=nome, 
                    email=email, 
                    password=senha
                )

                # Verifica se o grupo "nutricionista" existe, se não, cria
                nutricionista_group, created = Group.objects.get_or_create(name='nutricionista')
                # Adiciona o usuário ao grupo "nutricionista"
                user.groups.add(nutricionista_group)


                user.save()
                messages.success(request, 'Cadastro realizado com sucesso')
                return redirect('login')
    
    return render(request, 'usuarios/cadastroNutricionista.html', {'form': form})

def cadastroPa(request):
    form = CadastroFormsPa()

    if request.method == 'POST':
        form = CadastroFormsPa(request.POST)
        
        if form.is_valid():
            #pega os dados do formulário
            nome = form.cleaned_data['nomeCadastro']
            email = form.cleaned_data['emailCadastro']
            senha = form.cleaned_data['senhaCadastro']

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email já cadastrado')
            elif User.objects.filter(username=nome).exists():
                messages.error(request, 'Nome de usuário já existe')
            else:
                user = User.objects.create_user(username=nome, email=email,  password=senha)

                # Verifica se o grupo "paciente" existe, se não, cria
                paciente_group, created = Group.objects.get_or_create(name='paciente')
                # Adiciona o usuário ao grupo "paciente"
                user.groups.add(paciente_group)

                user.save()
                messages.success(request, 'Cadastro realizado com sucesso')
                return redirect('login')
    
    return render(request, 'usuarios/cadastroPaciente.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Deslogado com sucesso!')
    return redirect('login')

def cadastroTabela(request):
    return render(request, '/admin/galeria/tabelanutricional/add/')

def tabela_nutricional_view(request, username):
    try:
        tabela = TabelaNutricional.objects.get(usuarioReferencia__username=username)
        return render(request, 'usuarios/tabelaNutricional.html', {'tabela': tabela})
    except TabelaNutricional.DoesNotExist:
        return render(request, 'usuarios/tabelaNutricional.html', {'message': 'Tabela Nutricional não encontrada para o usuário.'})
