from django.urls import path
from apps.usuarios.views import login, cadastroPa, cadastroNutricionista, logout

urlpatterns = [ 
    
    path('login',login, name='login'),
    path('cadastroPaciente',cadastroPa, name='cadastroPaciente'),
    path('cadastroNutricionista',cadastroNutricionista, name='cadastroNutricionista'),
    path('logout',logout, name='logout')
]