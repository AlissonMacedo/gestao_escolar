# Generated by Django 2.1.4 on 2019-01-31 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extra', '0003_registrohoraextra_horas'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrohoraextra',
            name='ultilizada',
            field=models.BooleanField(default=False),
        ),
    ]