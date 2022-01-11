from django.contrib import admin

from .models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    fields = ('categoria', 'nome', 'qtd_estoque', 'preco')
    list_display = [ 'nome', 'categoria', 'qtd_estoque', 'preco'] 
    search_fields = ['nome'] 
    list_filter = ['categoria']
    list_editable = ['categoria', 'qtd_estoque', 'preco']


admin.site.register(Produto, ProdutoAdmin)