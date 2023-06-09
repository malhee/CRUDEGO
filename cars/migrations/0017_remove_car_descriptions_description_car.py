# Generated by Django 4.2.2 on 2023-06-09 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0016_alter_car_descriptions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='descriptions',
        ),
        migrations.AddField(
            model_name='description',
            name='car',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='descriptions', to='cars.car'),
        ),
    ]