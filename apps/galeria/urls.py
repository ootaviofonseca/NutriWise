from django.urls import path
from apps.galeria.views import index

urlpatterns = [
    path('',index, name='index'),
    
]