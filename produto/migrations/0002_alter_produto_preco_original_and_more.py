# Generated by Django 4.2.5 on 2023-09-09 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco_original',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_promocional',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]