# Generated by Django 4.1.4 on 2023-02-14 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_parcelamento', '0009_parcelas_nome_cliente_alter_parcelas_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendas',
            name='documento',
        ),
        migrations.DeleteModel(
            name='Parcelas',
        ),
        migrations.DeleteModel(
            name='Vendas',
        ),
    ]
