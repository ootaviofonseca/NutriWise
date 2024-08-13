from django.urls import path
from apps.usuarios.views import login, cadastroPa, cadastroNutricionista, logout, cadastroTabela, tabela_nutricional_view

urlpatterns = [ 
    
    path('login',login, name='login'),
    path('cadastroPaciente',cadastroPa, name='cadastroPaciente'),
    path('cadastroNutricionista',cadastroNutricionista, name='cadastroNutricionista'),
    path('cadastroTabela',cadastroTabela, name='cadastroTabela'),
    
    path('tabelaNutricional/<str:username>', tabela_nutricional_view, name='tabelaNutricional'),
    path('logout',logout, name='logout')

]