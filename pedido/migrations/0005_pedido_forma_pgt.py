# Generated by Django 4.2.5 on 2023-10-02 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0004_remove_pedido_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='forma_pgt',
            field=models.CharField(default='null', max_length=255),
        ),
    ]