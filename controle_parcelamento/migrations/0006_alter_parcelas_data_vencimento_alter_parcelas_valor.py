# Generated by Django 4.1.4 on 2023-02-12 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_parcelamento', '0005_remove_cliente_data_analise_cliente_modelo_negocio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcelas',
            name='data_vencimento',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Vencimento'),
        ),
        migrations.AlterField(
            model_name='parcelas',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Valor'),
        ),
    ]
