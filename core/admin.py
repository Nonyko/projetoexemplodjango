from django.contrib import admin

# Register your models here.
from .models import Pessoa

class PessoaModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome',)


admin.site.register(Pessoa, PessoaModelAdmin)