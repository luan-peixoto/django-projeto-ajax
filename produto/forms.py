from django import forms

from produto.models import Produto
from categoria.models import Categoria

class CadastraProdutoForm(forms.ModelForm):
    
    class Meta:
        model = Produto
        fields = ('categoria','nome', 'qtd_estoque', 'preco')

    nome = forms.CharField(
        error_messages = {'required' : 'Campo obrigatório.', 'unique' : 'Campo duplicado.'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '100'}),
    )

    categoria = forms.ModelChoiceField(
        error_messages = {'required' : 'Campo obrigatório.'},
        queryset = Categoria.objects.all().order_by('nome'),
        empty_label = "selecione uma categoria...",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm', 'maxlength': '70'}),
    )

    qtd_estoque = forms.IntegerField(
        min_value = 0,
        error_messages = {'required' : 'Campo obrigatório.', 'invalid': 'Quantidade inválida.',
        'min_value': 'O valor minimo é 0.', 'max_digits' : 'Atingiu numero máximo de digitos.',
        },

        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-sm',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44'})

    )
    
    preco = forms.DecimalField(
        localize = True,
        min_value = 0,
        error_messages = {'required' : 'Campo obrigatório.', 'invalid': 'Preço invalido.',
        'min_value': 'O valor minimo é 0.', 'max_digits' : 'Atingiu numero máximo de digitos.',
        'max_decimal_places': 'Mais de dois dígitos decimais', 'max_whole_digits':'Mais de 3 inteiros.'},

        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-sm',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44'})

    )

class QuantidadeForm(forms.Form):

    produto_id = forms.CharField(widget=forms.HiddenInput())

    quantidade = forms.IntegerField(
        min_value=0,
        max_value=99,
        widget=forms.TextInput(
            attrs={
                'class': 'form-quantidade form-control btn-secondary', 
                'style': 'text-align: center; color: black; background-color: rgb(254, 254, 254); width: 70px;',
                'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57)'
                }
            ),
        required=True
    )
