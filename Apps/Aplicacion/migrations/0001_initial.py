# Generated by Django 4.0.6 on 2022-07-09 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fabrica',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ubicacion', models.CharField(max_length=15, null=True)),
                ('nuc_numero', models.CharField(max_length=15, null=True)),
            ],
        ),
    ]
