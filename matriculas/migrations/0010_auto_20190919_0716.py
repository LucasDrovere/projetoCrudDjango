# Generated by Django 2.2.5 on 2019-09-19 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matriculas', '0009_auto_20190918_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos/'),
        ),
    ]