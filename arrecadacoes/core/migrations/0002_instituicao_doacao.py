# Generated by Django 5.0.4 on 2024-06-08 13:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('chave_pix', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_doacao', models.DateField(auto_now_add=True)),
                ('donante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.instituicao')),
            ],
        ),
    ]
