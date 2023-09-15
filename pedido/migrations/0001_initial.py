# Generated by Django 4.2.5 on 2023-09-15 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=255)),
                ('produto_id', models.CharField(max_length=255)),
                ('preco', models.FloatField()),
                ('quantidade', models.PositiveIntegerField()),
                ('imagem', models.CharField(max_length=2000)),
                ('subtotal', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('A', 'Aprovado'), ('p', 'Producão'), ('d', 'Despachado'), ('F', 'Finalizado')], default='C', max_length=1)),
            ],
        ),
    ]
