# Generated by Django 2.1.7 on 2019-04-16 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0008_auto_20190410_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='matricula',
            name='status_coordenacao',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='matricula',
            name='status_financeiro',
            field=models.BooleanField(default=False),
        ),
    ]
