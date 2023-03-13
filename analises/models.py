from django.db import models
from controle_parcelamento.models import Cliente

# Create your models here.
TIPOS_PROPOSTA_CHOICES = (
    ('Limites de Crédito','Limites de Crédito'),
    ('Venda Única','Venda Única'),
)

# class Analises(models.Model):
    
#     '''
#     cliente existente: define se o cliente já existe na tabela de clientes
#     '''
    
#     id = models.AutoField(primary_key=True)
#     cliente_existente = models.BooleanField('Cliente Existente', default=False)
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
#     documento = models.CharField('CPF/CNPJ', max_length=14)
#     nome = models.CharField('Nome do Cliente', max_length=100, null=False)
#     nivel_risco = models.CharField('Nível de Risco', max_length=100, null=False, blank=False)
#     modelo_negocio = models.CharField('Modelo de Negócio', max_length=100, null=True, blank=True)
#     data_analise = models.DateField('Data da Análise', null=True, blank=True)
    
#     tipo_proposta = models.CharField('Tipo de Proposta', max_length=40, null=True, blank=True, choices=TIPOS_PROPOSTA_CHOICES)
    
#     # limite_credito = models.FloatField('Limite de Crédito', null=True, blank=True)
#     valor_proposta = models.FloatField('Valor da Proposta', null=True, blank=True)
#     valor_concedido = models.FloatField('Valor Concedido', null=True, blank=True)

#     def __str__(self):
#         return self.nome
    
#     class Meta:
#         db_table = 'Analises'