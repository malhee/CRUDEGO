# Generated by Django 4.2.2 on 2023-06-09 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0024_alter_car_model_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='model_year',
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]