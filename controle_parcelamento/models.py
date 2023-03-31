from django.db import models

# Create your models here.

class Cliente(models.Model):
    
    NIVEL_RISCO_CHOICES = (
        ('Baixo','Baixo'),
        ('Baixíssimo','Baixíssimo'),
        ('Médio','Médio'),
        ('Alto','Alto'),
        ('Altíssimo','Altíssimo'),
    )

    MODELO_NEGOCIO_CHOICES = (
        ('Sol Copérnico','Sol Copérnico'),
        ('Sol+','Sol+'),
    )
    # id = models.AutoField(primary_key=True)
    documento = models.CharField('CPF/CNPJ', primary_key=True, max_length=14)
    nome = models.CharField('Nome do Cliente', max_length=100, null=False)
    nivel_risco = models.CharField('Nível de Risco', max_length=100, choices=NIVEL_RISCO_CHOICES, null=False, blank=False)
    modelo_negocio = models.CharField('Modelo de Negócio', choices=MODELO_NEGOCIO_CHOICES, max_length=100, null=True, blank=True)
    data_analise = models.DateField('Data da Análise', null=True, blank=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'Cliente'
    



class Vendas(models.Model):

    VENDAS_STATUS_CHOICES = (
        ('Entregue','Entregue'),
        ('Em processo de entrega','Em processo de entrega'),
        ('Aguardando expedição','Aguardando expedição'),
        ('Em processo triagem','Em processo triagem')
    )

    PEDIDOS_STATUS_CHOICES = (
        ('Concluido','Concluido'),
        ('Em atraso','Em atraso'),
        ('Em andamento','Em andamento'),
        ('Renegociado','Renegociado')
    )

    id = models.AutoField(primary_key=True)
    num_pedido = models.CharField('Número do Pedido',max_length=30, null=False, blank=False, unique=True, default=None)
    documento = models.ForeignKey(Cliente,verbose_name='Nome Cliente', on_delete=models.CASCADE, null=False, blank=False)
    data_pedido = models.DateField('Data do Pedido', null=False, blank=False)
    valor_pedido = models.DecimalField('Valor do Pedido', max_digits=10, decimal_places=2, null=False, blank=False)
    valor_entrada = models.DecimalField('Valor da Entrada', max_digits=10, decimal_places=2, null=False, blank=False)
    valor_parcelado = models.DecimalField('Valor Parcelado', max_digits=10, decimal_places=2, null=True, blank=True)
    qnt_parcelas = models.IntegerField('Quantidade de Parcelas', null=False, blank=False)
    status = models.CharField('Status do Pedido', max_length=100, choices=VENDAS_STATUS_CHOICES, null=True, blank=True)
    status_venda = models.CharField('Status da Venda', max_length=100, choices=PEDIDOS_STATUS_CHOICES, null=True, blank=True)
    
    def __str__(self):
        return self.num_pedido
    
    class Meta:
        db_table = 'Vendas'





class Parcelas(models.Model):

    PARCELAS_STATUS_CHOICES = (
        ('Em Atraso','Em Atraso'),
        ('Em Aberto','Em Aberto'),
        ('Pago','Pago'),
        ('Pago em Atraso','Pago em Atraso'),
        ('Vencido','Vencido'),
        ('Cancelado','Cancelado')
    )
    
    id = models.AutoField(primary_key=True)
    venda = models.ForeignKey(Vendas, on_delete=models.CASCADE, null=True, blank=True)
    num_pedido = models.CharField('Número do Pedido',max_length=30, null=True, blank=True)
    nome_cliente = models.CharField('Nome do Cliente', max_length=50, null=True, blank=True)
    parcela = models.IntegerField('Parcela', null=False, blank=False)
    data_vencimento = models.DateField('Data de Vencimento', null=True, blank=True)
    status = models.CharField('Status', max_length=100, choices=PARCELAS_STATUS_CHOICES ,null=True, blank=True)
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return str(self.parcela)
    
    class Meta:
        db_table = 'Parcelas'