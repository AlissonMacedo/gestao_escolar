# Generated by Django 2.1.7 on 2019-04-09 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0006_auto_20190409_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='matricula',
            name='varlorparcelas',
            field=models.IntegerField(blank=True, default=1, verbose_name='Valor Parcelas '),
            preserve_default=False,
        ),
    ]