from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages


from apps.galeria.models import TabelaNutricional

def index(request):
    if not request.user.is_authenticated:
       messages.error(request, 'Você precisa estar logado para acessar essa página')
       return redirect('login')
    return render(request,'galeria/index.html')


