# Generated by Django 4.2.2 on 2023-12-30 21:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Província')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Produto')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Preço')),
                ('data_validade', models.DateField()),
                ('loja', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Parceria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parceiro', models.CharField(default='Nenhum', help_text='Escreva o seu nome de usuário', max_length=100)),
                ('contato', models.IntegerField()),
                ('data_realizacao', models.DateTimeField(default=datetime.datetime(2023, 12, 30, 22, 57, 6, 402109))),
                ('estado', models.CharField(choices=[('DISPINÍVEL', 'Disponível'), ('EFECTUADA', 'Efetuada')], default='Disponível', max_length=20, verbose_name='Estado da Parceria')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.produto')),
                ('proprietario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Município')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.provincia', verbose_name='Província')),
            ],
        ),
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Bairro')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.municipio', verbose_name='Município')),
            ],
        ),
    ]