# Generated by Django 2.1.7 on 2019-04-12 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensalidades',
            name='status_mensalidades',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='financeiro.Status_mensalidades'),
            preserve_default=False,
        ),
    ]
