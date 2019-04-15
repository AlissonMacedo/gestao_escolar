# Generated by Django 2.1.7 on 2019-04-12 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aluno', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensalidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aluno.Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='Status_mensalidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=18)),
            ],
        ),
    ]
