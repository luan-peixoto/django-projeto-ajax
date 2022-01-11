from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from produto.forms import CadastraProdutoForm, QuantidadeForm
from produto.models import Produto

def index(request):
    produtos = Produto.objects.all().order_by('id')
    # carrega os produtos
    total = 0
    lista_de_forms_qtd = []
    for produto in produtos:
        total += (produto.qtd_estoque * produto.preco)
        # incrementa o total do preço dos produtos
        lista_de_forms_qtd.append(QuantidadeForm(initial= {'quantidade': produto.qtd_estoque, 'produto_id': produto.id}))
        # cria um formulário de quantidade e id para cada produto

    cadastro_produto_form = CadastraProdutoForm()
    # gera um formulário de cadastro vazio

    return render(request, "./index.html", {'form': cadastro_produto_form, 'produtos': zip(produtos, lista_de_forms_qtd), 
    'total': total})
    # render transforma todo o código em uma https response contendo o html final da página


def cadastrarProduto(request):
    if request.POST:
        cadastro_produto_form = CadastraProdutoForm(request.POST)
        # cria um formulário com os dados enviados
        if cadastro_produto_form.is_valid():
            produto_cadastrado = cadastro_produto_form.save()
            # caso os dados sejam válidos, salva um novo produto
        
            produtos = Produto.objects.all().order_by('id')
            total = 0
            for produto in produtos:
                total += (produto.qtd_estoque * produto.preco)
            # recupera o preço total dos produtos
            pagina = render(request, "./formulario_cadastro.html", {'form': CadastraProdutoForm()}).content.decode("utf-8")
            # renderiza um formulário de cadastro limpo
            form_qtd_inputs = QuantidadeForm(initial= {'quantidade': produto.qtd_estoque, 'produto_id': produto.id})
            # cria dois inputs, um como formulário de quantidade, outro como id

            form_qtd_input = str(form_qtd_inputs['quantidade'])
            form_id_input = str(form_qtd_inputs['produto_id'])
            # transforma os inputs em elemento html
            return JsonResponse({'form_id_input': form_id_input, 'form_qtd_input': form_qtd_input, 'id': produto_cadastrado.id, 'nome': produto_cadastrado.nome, 'categoria': produto_cadastrado.categoria.nome, 'quantidade': produto_cadastrado.qtd_estoque, 'preco': produto_cadastrado.preco, 'total': total, 'pagina': pagina})
            # retorna um json response contendo o produto adicionado, o preço total dos produtos, os valores do produto, e os inputs com id e qtd
        else:
            return render(request, "./formulario_cadastro.html", {'form': cadastro_produto_form})
            # caso os dados sejam inválidos renderiza o formulário de cadastro novamente e envia como HttpsResponse


def removerProduto(request):
    if request.POST:
        # caso seja um request post
        id = request.POST.get("id")
        produto = get_object_or_404(Produto, pk=id)
        produto.delete()
        # recupera o produto e deleta

        produtos = Produto.objects.all().order_by('id')
        total = 0
        for produto in produtos:
            total += (produto.qtd_estoque * produto.preco)
        # atualiza o preço total dos produtos

        return JsonResponse({'total': total})
        # retorna um json response contendo o preço
    else:
        return HttpResponse('')
        # retorna um http response vazio

def alterarProduto(request):
    if request.POST:
        # caso seja um request post
        id = request.POST.get("id")
        qtd = request.POST.get("quantidade")
        produto = get_object_or_404(Produto, pk=id)
        produto.qtd_estoque = qtd
        produto.save()
        # recupera o produto e deleta

        produtos = Produto.objects.all().order_by('id')
        total = 0
        for produto in produtos:
            total += (produto.qtd_estoque * produto.preco)
        # atualiza o preço total dos produtos

        return JsonResponse({'total': total})
        # retorna um json response contendo o preço
    else:
        return HttpResponse('')