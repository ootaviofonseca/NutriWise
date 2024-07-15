from django.urls import path
from apps.usuarios.views import loginPa,loginAdm, cadastroPa, cadastroAdm, logout

urlpatterns = [ 
    path('loginPaciente',loginPa, name='loginPaciente'),
    path('loginAdm',loginAdm, name='loginAdm'),
    path('cadastroPaciente',cadastroPa, name='cadastroPaciente'),
    path('cadastroAdm',cadastroAdm, name='cadastroAdm'),
    path('logout',logout, name='logout')
]