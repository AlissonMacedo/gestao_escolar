# Generated by Django 2.1.7 on 2019-03-11 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('secretaria', '0001_initial'),
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='projetor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numerodeserie', models.CharField(blank=True, max_length=100, null=True)),
                ('nome', models.CharField(max_length=100)),
                ('observacao', models.TextField(blank=True, null=True, verbose_name='Observação')),
                ('status', models.CharField(choices=[('QUEBRADO', 'Quebrado'), ('OK', 'Ok'), ('EM MANUTENÇÃO', 'Em manutenção')], default='AGUARDANDO', max_length=20)),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='empresas.Empresa')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='secretaria.SalaDeAula')),
            ],
        ),
    ]
