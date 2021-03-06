# Generated by Django 2.1.7 on 2019-03-19 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tecnologiadainformacao', '0001_initial'),
        ('documentos', '0002_auto_20190311_0111'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentoAluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('arquivo', models.FileField(upload_to='documentosAlunos')),
                ('pertense', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tecnologiadainformacao.projetor')),
            ],
        ),
        migrations.AlterField(
            model_name='documento',
            name='pertense',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aluno.Aluno'),
        ),
        migrations.AlterField(
            model_name='documentoprojetor',
            name='arquivo',
            field=models.FileField(upload_to='documentosProjetor'),
        ),
    ]
