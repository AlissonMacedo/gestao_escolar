# Generated by Django 2.1.7 on 2019-04-10 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0011_auto_20190401_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='segundonome',
            field=models.CharField(default=1, max_length=18),
            preserve_default=False,
        ),
    ]