# Generated by Django 3.0.5 on 2020-04-11 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='empleados_asignados',
            field=models.ManyToManyField(to='app.Empleado'),
        ),
        migrations.DeleteModel(
            name='AsignacionTarea',
        ),
    ]