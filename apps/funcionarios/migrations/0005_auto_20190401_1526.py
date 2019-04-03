# Generated by Django 2.1.7 on 2019-04-01 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0002_departamento_empresa'),
        ('funcionarios', '0004_auto_20190106_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='departamento',
        ),
        migrations.AddField(
            model_name='funcionario',
            name='departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='departamentos.Departamento'),
        ),
    ]