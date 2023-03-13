from django.forms import ModelForm
from controle_parcelamento.models import Cliente, Vendas, Parcelas
from django import forms

from controle_parcelamento.models import *

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from crispy_forms.layout import Submit


class CreateClienteForm(ModelForm):
    
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'data_analise': forms.TextInput(attrs={'type': 'date','required': False}),
            
        }
        
        
class CreateVendasForm(ModelForm):
     
    data_pedido = forms.DateField(label="Data do Pedido",widget=forms.TextInput(attrs={'type': 'date','required': False}))
    
    documento = forms.ModelChoiceField(
        queryset=Cliente.objects.order_by('nome'),
        empty_label='-------------------',
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Nome do Cliente'
    )
    
    def clean_valor_pedido(self):
        cleaned_data = super().clean()
        valor_pedido = cleaned_data.get("valor_pedido")
        if ',' in str(valor_pedido):
            valor_pedido = valor_pedido.replace(',','.')
        return valor_pedido
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        instance.valor_parcelado = instance.valor_pedido - instance.valor_entrada
        instance.save()
        venda = Vendas.objects.get(num_pedido=instance.num_pedido)
        
        lista_parcelas = [Parcelas(venda=venda,
                                   num_pedido=venda.num_pedido,
                                   parcela=i + 1,
                                   nome_cliente=venda.documento,
                                   valor=instance.valor_parcelado / instance.qnt_parcelas,
                                   status='Em Aberto') for i in range(instance.qnt_parcelas)]
            
        Parcelas.objects.bulk_create(lista_parcelas)
        return instance

    class Meta:
        model = Vendas
        fields = ['num_pedido', 
                  'documento', 
                  'data_pedido',
                  'valor_pedido', 
                  'valor_entrada', 
                #   'valor_parcelado', 
                  'qnt_parcelas',
                  'status'
                ]


class UpdateClienteForm(ModelForm):
    
    class Meta:
        model = Cliente
        fields = [
            'documento',
            'nome',
            'nivel_risco',
            'modelo_negocio',
            'data_analise',            
        ]
        widgets = {
            'documento': forms.TextInput(attrs={'readonly': 'readonly'}),
            'data_analise': forms.TextInput(attrs={'type': 'date','required': False}),
        }
        

class UpdateVendasForm(ModelForm):
    
    class Meta:
        model = Vendas
        fields = '__all__'
        widgets = {
            'data_pedido': forms.TextInput(attrs={'type': 'date','required': False}),
        }
        
        
class UpdateParcelasForm(ModelForm):
    
    class Meta:
        model = Parcelas
        fields = [
            'data_vencimento',
            'valor',
            'status'
        ]
        widgets = {
            'data_vencimento': forms.TextInput(attrs={'type': 'date','required': False}),
        }