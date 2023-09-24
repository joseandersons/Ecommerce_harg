# Generated by Django 4.2.5 on 2023-09-23 22:27

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.usuario')),
                ('cnpj', models.CharField(blank=True, max_length=18, null=True)),
                ('pausado', models.CharField(default='N', max_length=1)),
                ('horario_abertura', models.TimeField(blank=True, null=True)),
                ('horario_fechamento', models.TimeField(blank=True, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='loja_imagens/%Y/%m')),
                ('tipo_culinaria', models.CharField(choices=[('BR', 'Brasileira'), ('IT', 'Italiana'), ('AM', 'Americana'), ('JP', 'Japonesa'), ('OU', 'Outra')], default='OU', max_length=2)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('core.usuario',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
