# Generated by Django 4.2.5 on 2023-10-01 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0002_pedido_loja_alter_itempedido_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='total',
            field=models.FloatField(default=0.0),
        ),
    ]