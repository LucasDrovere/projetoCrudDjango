# Generated by Django 2.2.5 on 2019-09-18 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matriculas', '0003_auto_20190918_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='dt_nascimento',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data de nascimento'),
        ),
    ]
