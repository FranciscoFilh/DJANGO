from django.contrib import admin
from .models import Carne

class ListCarnes(admin.ModelAdmin):
    list_display = ('nome_da_carne', 'tipos_da_carne', 'data_do_corte', 'fazenda_que_vendeu_a_carne', 'preco',)

admin.site.register(Carne, ListCarnes)
