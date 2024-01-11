# Generated by Django 5.0.1 on 2024-01-11 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_livro', models.CharField(max_length=100)),
                ('ano_da_publicacao', models.IntegerField(max_length=4)),
                ('quantidade_de_paginas', models.IntegerField(max_length=3)),
                ('nome_do_autor', models.CharField(max_length=20)),
                ('nome_da_editora', models.CharField(max_length=20)),
                ('preco', models.FloatField(default=0.0)),
            ],
        ),
    ]
