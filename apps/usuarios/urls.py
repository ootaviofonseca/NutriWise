from django.urls import path
from apps.usuarios.views import login, cadastroPa, cadastroNutricionista, logout, cadastroTabela

urlpatterns = [ 
    
    path('login',login, name='login'),
    path('cadastroPaciente',cadastroPa, name='cadastroPaciente'),
    path('cadastroNutricionista',cadastroNutricionista, name='cadastroNutricionista'),
    path('cadastroTabela',cadastroTabela, name='cadastroTabela'),
    path('logout',logout, name='logout')

]