# Generated by Django 2.1.7 on 2019-03-11 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeironome', models.CharField(max_length=30, verbose_name='Nome')),
                ('segundonome', models.CharField(max_length=30, verbose_name='Sobrenome')),
                ('idade', models.IntegerField(blank=True, null=True, verbose_name='Idade')),
                ('cpf', models.IntegerField(blank=True, null=True, verbose_name='CPF')),
                ('RG', models.IntegerField(blank=True, null=True, verbose_name='RG')),
                ('datadenascimento', models.DateTimeField(blank=True, null=True, verbose_name='Data Nascimento')),
                ('cursoApto', models.CharField(blank=True, max_length=60, null=True, verbose_name='curso Apto')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='professor_photo')),
                ('observacao', models.TextField(blank=True, null=True, verbose_name='Observação')),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='empresas.Empresa')),
            ],
            options={
                'verbose_name': 'Professor',
                'verbose_name_plural': 'Professores',
                'ordering': ['primeironome'],
            },
        ),
    ]