# Generated by Django 4.0.6 on 2022-07-19 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0007_producto_imagenproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagenProducto',
            field=models.ImageField(null=True, upload_to='imagenes/'),
        ),
    ]
