# Generated by Django 2.1.7 on 2019-04-16 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='telefone',
            field=models.IntegerField(blank=True, null=True, verbose_name='Telefone'),
        ),
    ]