from django.contrib import admin
from django.urls import path
from projeto import views

urlpatterns = [
    path('', views.index, name="index"),  
    path('cadastrar_produto/', views.cadastrarProduto, name="cadastrar_produto"),  
    path('remover_produto/', views.removerProduto, name="remover_produto"),    
    path('alterar_produto/', views.alterarProduto, name="alterar_produto"),  
    path('admin/', admin.site.urls),
]