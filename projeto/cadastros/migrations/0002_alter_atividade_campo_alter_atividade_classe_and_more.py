# Generated by Django 4.1.5 on 2023-01-27 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='campo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.campo', verbose_name='Fornecedor'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='classe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.classe', verbose_name='Projeto'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.status', verbose_name='Vaga'),
        ),
    ]