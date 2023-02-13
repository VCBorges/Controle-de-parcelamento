from django.forms import ModelForm
from controle_parcelamento.models import Cliente, Vendas, Parcelas
from django import forms

from controle_parcelamento.models import *

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field


class CreateClienteForm(ModelForm):
    
    data_analise = forms.DateField(label="Data da Análise",widget=forms.TextInput(attrs={'type': 'date','required': True}))
    
    class Meta:
        model = Cliente
        fields = '__all__'
        
        
class CreateVendasForm(ModelForm):
    
    data_pedido = forms.DateField(label="Data do Pedido",widget=forms.TextInput(attrs={'type': 'date','required': True}))
    
    # def __init__(self, *args, **kwargs):
    #     super(CreateVendasForm, self).__init__(*args, **kwargs)

    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Field('data_pedido', attrs={'type': 'date'}),
    #     )
    
    def save(self, commit=True):
        instance = super().save()
        
        lista_parcelas = []
        
        venda = Vendas.objects.get(num_pedido=instance.num_pedido)
        
        # print(venda.documento)
        
        # cliente = Cliente.objects.get(documento=venda.documento)
        
        
        for i in range(instance.qnt_parcelas):
            
            parcela = Parcelas(num_pedido=venda,
                               parcela=i + 1,
                               nome_cliente=venda.documento,
                               valor=instance.valor_parcelado/instance.qnt_parcelas,
                               status='Em Aberto')
            
            lista_parcelas.append(parcela)
        Parcelas.objects.bulk_create(lista_parcelas)
        
        # if commit:
            # instance.save()
        return instance

    class Meta:
        model = Vendas
        fields = ['num_pedido', 
                  'documento', 
                  'data_pedido',
                  'valor_pedido', 
                  'valor_entrada', 
                  'valor_parcelado', 
                  'qnt_parcelas',
                  'status'
                ]


class UpdateClienteForm(ModelForm):
    
    class Meta:
        model = Cliente
        fields = '__all__'
        

class UpdateVendasForm(ModelForm):
    
    class Meta:
        model = Vendas
        fields = '__all__'
        
        
class UpdateParcelasForm(ModelForm):
    
    data_vencimento = forms.DateField(label="Data do Pedido",widget=forms.TextInput(attrs={'type': 'date'}))
        
    class Meta:
        model = Parcelas
        fields = '__all__'