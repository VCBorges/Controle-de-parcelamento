# Generated by Django 4.1.4 on 2023-02-15 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_parcelamento', '0016_alter_cliente_modelo_negocio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nivel_risco',
            field=models.CharField(choices=[('Baixissimo', 'Baixíssimo'), ('Medio', 'Médio'), ('Alto', 'Alto'), ('Altissimo', 'Altíssimo')], max_length=100, verbose_name='Nível de Risco'),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='num_pedido',
            field=models.CharField(default=None, max_length=30, unique=True, verbose_name='Número do Pedido'),
        ),
    ]
