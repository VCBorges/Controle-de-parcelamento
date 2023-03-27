from django.db import models
from controle_parcelamento.models import Cliente

# Create your models here.

class Analises(models.Model):
    
    '''
    #* Cliente existente: define se o cliente já existe na tabela de clientes
    '''
    
    TIPOS_PROPOSTA_CHOICES = (
        ('Limites de Crédito','Limites de Crédito'),
        ('Venda Única','Venda Única'),
    )
    
    MODELO_NEGOCIO_CHOICES = (
        ('Sol Copérnico','Sol Copérnico'),
        ('Sol+','Sol+'),
    )
    
    NIVEL_RISCO_CHOICES = (
        ('Baixo','Baixo'),
        ('Baixíssimo','Baixíssimo'),
        ('Médio','Médio'),
        ('Alto','Alto'),
        ('Altíssimo','Altíssimo'),
    )
    
    TIPOS_PROPOSTA_CHOICES = (
        ('Venda Única','Venda Única'),
        ('Limite de Crédito','Limite de Crédito'),
    )
    
    id = models.AutoField(primary_key=True)
    cliente = models.CharField('Cliente', max_length=100, null=False)
    documento = models.CharField('CPF/CNPJ', max_length=14)
    nivel_risco = models.CharField('Nível de Risco', max_length=100, choices=NIVEL_RISCO_CHOICES ,null=False, blank=False)
    modelo_negocio = models.CharField('Modelo de Negócio', max_length=100, choices=MODELO_NEGOCIO_CHOICES, null=True, blank=True)
    tipo_proposta = models.CharField('Tipo de Proposta', max_length=40, null=True, blank=True, choices=TIPOS_PROPOSTA_CHOICES)
    valor_proposta = models.DecimalField('Valor da Proposta', max_digits=10, decimal_places=2, null=True, blank=True)
    valor_concedido = models.DecimalField('Valor Concedido', max_digits=10, decimal_places=2, null=True, blank=True)
    data_inicio = models.DateField('Data de Início', null=True, blank=True)
    data_entrega = models.DateField('Data de Entrega', null=True, blank=True)

    def __str__(self):
        return self.cliente
    
    class Meta:
        db_table = 'Analises'
