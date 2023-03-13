# Generated by Django 4.1.4 on 2023-02-27 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_parcelamento', '0022_alter_parcelas_id_venda_alter_parcelas_num_pedido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parcelas',
            old_name='id_venda',
            new_name='venda',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nivel_risco',
            field=models.CharField(choices=[('Baixo', 'Baixo'), ('Baixíssimo', 'Baixíssimo'), ('Médio', 'Médio'), ('Alto', 'Alto'), ('Altíssimo', 'Altíssimo')], max_length=100, verbose_name='Nível de Risco'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome do Cliente'),
        ),
        migrations.AlterField(
            model_name='parcelas',
            name='status',
            field=models.CharField(blank=True, choices=[('Em Atraso', 'Em Atraso'), ('Em Aberto', 'Em Aberto'), ('Pago', 'Pago'), ('Pago em Atraso', 'Pago em Atraso'), ('Vencido', 'Vencido'), ('Cancelado', 'Cancelado')], max_length=100, null=True, verbose_name='Status'),
        ),
    ]