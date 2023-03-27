# Generated by Django 4.1.4 on 2023-03-26 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_parcelamento', '0023_rename_id_venda_parcelas_venda_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendas',
            name='status_venda',
            field=models.CharField(blank=True, choices=[('Concluido', 'Concluido'), ('Em atraso', 'Em atraso'), ('Em andamento', 'Em andamento'), ('Renegociado', 'Renegociado')], max_length=100, null=True, verbose_name='Status da Venda'),
        ),
    ]