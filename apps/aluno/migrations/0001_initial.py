# Generated by Django 2.1.7 on 2019-02-17 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('primeironome', models.CharField(max_length=30, verbose_name='Nome')),
                ('segundonome', models.CharField(max_length=30, verbose_name='Sobrenome')),
                ('idade', models.IntegerField(verbose_name='Idade')),
                ('cpf', models.IntegerField(blank=True, null=True, verbose_name='CPF')),
                ('RG', models.IntegerField(blank=True, null=True, verbose_name='RG')),
                ('datadenascimento', models.DateTimeField(verbose_name='Data Nascimento')),
                ('responsavel', models.CharField(max_length=30, verbose_name='Responsavel')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='empresas.Empresa')),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
                'ordering': ['id'],
            },
        ),
    ]
