# Generated by Django 4.2.5 on 2023-09-11 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_alter_produto_preco_original_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco_original',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_promocional',
            field=models.CharField(default='0', max_length=10),
        ),
    ]
