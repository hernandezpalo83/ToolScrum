# Generated by Django 3.0.3 on 2020-05-22 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='descripcion',
            field=models.TextField(),
        ),
    ]