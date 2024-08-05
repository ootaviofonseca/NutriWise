from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.models import Group

def index(request):
    if not request.user.is_authenticated:
       messages.error(request, 'Você precisa estar logado para acessar essa página')
       return redirect('login')
    return render(request,'galeria/index.html')
