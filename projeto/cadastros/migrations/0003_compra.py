# Generated by Django 4.1.5 on 2023-01-27 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_alter_atividade_campo_alter_atividade_classe_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Torre', models.CharField(max_length=50)),
                ('Fornecedor', models.CharField(max_length=150)),
                ('Competencia', models.CharField(max_length=150)),
                ('Tipo', models.CharField(max_length=50)),
                ('Valor', models.CharField(max_length=50)),
            ],
        ),
    ]
