# Generated by Django 4.2.2 on 2023-06-09 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_car_description_delete_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='description',
        ),
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('carro', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
            ],
        ),
    ]
