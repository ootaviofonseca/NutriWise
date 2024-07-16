from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from apps.galeria.models import Administrador, Usuario, TabelaNutricional, Refeicoes

class ListandoAdministradores(admin.ModelAdmin):
    list_display = ('id', 'nome', 'senha')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10

class ListandoUsuarios(admin.ModelAdmin):
    list_display = ('nome', 'senha', 'cpf')
    list_display_links = ('nome', 'cpf')
    search_fields = ('nome', 'cpf')
    list_per_page = 10

class RefeicoesInline(admin.TabularInline):
    model = TabelaNutricional.refeicoes.through
    extra = 1

class ListandoTabelaNutricional(admin.ModelAdmin):
    list_display = ('usuarioReferencia', 'usuarioPeso', 'gorduraCorporal', 'objetivo')
    list_display_links = ('usuarioReferencia', 'usuarioPeso')
    search_fields = ('usuarioReferencia__nome',)
    list_per_page = 10
    inlines = [RefeicoesInline]

class ListandoRefeicoes(admin.ModelAdmin):
    list_display = ('alimento', 'quantidade', 'horario')
    list_display_links = ('alimento', 'horario')
    search_fields = ('alimento', 'horario')
    list_per_page = 10
    list_filter = ('alimento',)



admin.site.register(Administrador, ListandoAdministradores)
admin.site.register(Usuario, ListandoUsuarios)
admin.site.register(TabelaNutricional, ListandoTabelaNutricional)
admin.site.register(Refeicoes, ListandoRefeicoes)
