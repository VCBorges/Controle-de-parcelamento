# Generated by Django 4.1.4 on 2023-02-20 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controle_parcelamento', '0021_vendas_status_venda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcelas',
            name='id_venda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='controle_parcelamento.vendas'),
        ),
        migrations.AlterField(
            model_name='parcelas',
            name='num_pedido',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Número do Pedido'),
        ),
    ]