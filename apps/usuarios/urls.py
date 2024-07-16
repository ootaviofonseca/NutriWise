from django.urls import path
from apps.usuarios.views import login, cadastroPa, cadastroAdm, logout

urlpatterns = [ 
    
    path('login',login, name='login'),
    path('cadastroPaciente',cadastroPa, name='cadastroPaciente'),
    path('cadastroAdm',cadastroAdm, name='cadastroAdm'),
    path('logout',logout, name='logout')
]