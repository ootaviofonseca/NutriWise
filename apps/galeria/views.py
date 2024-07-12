from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


import os

def pageInicial(request):
    # Diretório da pasta atual (onde views.py está localizado)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Caminho absoluto para o template
    template_path = os.path.join(current_dir, '../../templates/index.html')
    
    # Carregar e renderizar o template
    with open(template_path, 'r') as file:
        template_content = file.read()
    
    return HttpResponse(template_content)