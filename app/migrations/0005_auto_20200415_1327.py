# Generated by Django 3.0.5 on 2020-04-15 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200415_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogo',
            name='nombre',
            field=models.CharField(default='NombreDefault', max_length=100),
        ),
        migrations.AddField(
            model_name='catalogo',
            name='precio',
            field=models.FloatField(default=0.0),
        ),
    ]
