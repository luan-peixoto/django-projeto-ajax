from django.contrib import admin

from .models import Categoria

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome'] 
admin.site.register(Categoria, CategoriaAdmin)