# Generated by Django 4.1.2 on 2022-10-26 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barsa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('nombre_del_club', models.CharField(max_length=200)),
                ('pais_club', models.CharField(max_length=200)),
                ('ciudad_representada', models.CharField(max_length=200)),
                ('edad', models.PositiveIntegerField(default=0)),
                ('titulos', models.CharField(max_length=200)),
                ('nombre_estadio', models.CharField(max_length=200)),
                ('capacidad_estadio', models.PositiveIntegerField(default=0)),
                ('presidente_club', models.CharField(max_length=200)),
            ],
        ),
    ]
