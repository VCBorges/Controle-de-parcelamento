from django.db import models

# Create your models here.
NIVEL_RISCO_CHOICES = (
    ('Baixissimo','Baixissimo'),
    ('Medio','Medio'),
    ('Alto','Alto'),
    ('Altissimo','Altissimo'),
)

MODELO_NEGOCIO_CHOICES = (
    ('Sol Copérnico','Sol Copernico'),
    ('Sol+','Sol+'),
)

class Cliente(models.Model):
    # id = models.AutoField(primary_key=True)
    documento = models.CharField('CPF/CNPJ', primary_key=True, max_length=14)
    nome = models.CharField('Nome do Cliente', max_length=50, null=False)
    nivel_risco = models.CharField('Nível de Risco', max_length=100, choices=NIVEL_RISCO_CHOICES, null=False, blank=False)
    modelo_negocio = models.CharField('Modelo de Negócio', choices=MODELO_NEGOCIO_CHOICES, max_length=100, null=True, blank=True)
    data_analise = models.DateField('Data da Análise', null=True, blank=True)

    def __str__(self):
        return self.nome

VENDAS_STATUS_CHOICES = (
    ('Entregue','Entregue'),
    ('Em processo de entrega','Em processo de entrega'),
    ('Aguardando expedição','Aguardando expedição'),
    ('Em processo triagem','Em processo triagem')
)

class Vendas(models.Model):
    num_pedido = models.CharField('Número do Pedido', primary_key=True, max_length=10, null=False, blank=False)
    documento = models.ForeignKey(Cliente,verbose_name='CPF/CNPJ', on_delete=models.CASCADE, null=False, blank=False)
    data_pedido = models.DateField('Data do Pedido', null=False, blank=False)
    valor_pedido = models.DecimalField('Valor do Pedido', max_digits=10, decimal_places=2, null=False, blank=False)
    valor_entrada = models.DecimalField('Valor da Entrada', max_digits=10, decimal_places=2, null=False, blank=False)
    valor_parcelado = models.DecimalField('Valor Parcelado', max_digits=10, decimal_places=2, null=False, blank=False)
    qnt_parcelas = models.IntegerField('Quantidade de Parcelas', null=False, blank=False)
    status = models.CharField('Status do Pedido', max_length=100, choices=VENDAS_STATUS_CHOICES, null=True, blank=True)
    
    def __str__(self):
        return self.num_pedido

parcelas_status_choices = (
    ('Em Atraso','Em Atraso'),
    ('Em Aberto','Em Aberto'),
    ('Pago','Pago'),
    ('Vencido','Vencido'),
    ('Cancelado','Cancelado')
)

class Parcelas(models.Model):
    id = models.AutoField(primary_key=True)
    num_pedido = models.ForeignKey(Vendas, on_delete=models.CASCADE, null=False, blank=False)
    nome_cliente = models.CharField('Nome do Cliente', max_length=50, null=True, blank=True)
    parcela = models.IntegerField('Parcela', null=False, blank=False)
    data_vencimento = models.DateField('Data de Vencimento', null=True, blank=True)
    status = models.CharField('Status', max_length=100, choices=parcelas_status_choices ,null=True, blank=True)
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return self.parcela
    


    


