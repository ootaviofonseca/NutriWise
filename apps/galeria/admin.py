from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from apps.galeria.models import  TabelaNutricional, Refeicoes





class RefeicoesInline(admin.TabularInline):
    model = TabelaNutricional.refeicoes.through
    extra = 1

class ListandoTabelaNutricional(admin.ModelAdmin):
    list_display = ('usuarioReferencia', 'usuarioPeso', 'gorduraCorporal', 'objetivo')
    list_display_links = ('usuarioReferencia', 'usuarioPeso')
    search_fields = ('usuarioReferencia__nome',)
    list_per_page = 10
    inlines = [RefeicoesInline]
    exclude = ('refeicoes',) 

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Se o usuário é superusuário, ele verá apenas os objetos que criou
        if request.user.is_superuser:
            return qs.filter(usuarioReferencia=request.user)
        return qs 
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.usuarioReferencia = request.user
        super().save_model(request, obj, form, change)

class ListandoRefeicoes(admin.ModelAdmin):
    list_display = ('alimento', 'quantidade', 'horario')
    list_display_links = ('alimento', 'horario')
    search_fields = ('alimento', 'horario')
    list_per_page = 10
    list_filter = ('alimento',)

admin.site.register(TabelaNutricional, ListandoTabelaNutricional)
admin.site.register(Refeicoes, ListandoRefeicoes)
