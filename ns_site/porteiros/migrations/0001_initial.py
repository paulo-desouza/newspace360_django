# Generated by Django 5.0.1 on 2024-01-19 18:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Porteiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=194, verbose_name='Nome Completo')),
                ('CPF', models.CharField(max_length=11, verbose_name='CPF')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone de Contato')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Porteiro',
                'verbose_name_plural': 'Porteiros',
                'db_table': 'porteiro',
            },
        ),
    ]
