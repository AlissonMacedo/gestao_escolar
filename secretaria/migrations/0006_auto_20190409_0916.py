# Generated by Django 2.1.7 on 2019-04-09 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0005_auto_20190403_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='preco',
            field=models.IntegerField(blank=True, verbose_name='preco'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='totalapagar',
            field=models.IntegerField(blank=True, verbose_name='total a pagar'),
        ),
    ]
