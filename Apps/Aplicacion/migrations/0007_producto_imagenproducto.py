# Generated by Django 4.0.6 on 2022-07-19 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0006_remove_suministrar_suministrar'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagenProducto',
            field=models.FileField(null=True, upload_to='imagenProducto'),
        ),
    ]