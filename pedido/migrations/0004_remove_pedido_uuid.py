# Generated by Django 4.2.5 on 2023-10-01 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_alter_pedido_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='uuid',
        ),
    ]
