# Generated by Django 4.1.5 on 2023-01-22 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChargingStation', '0003_remove_chargingstation_active_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargingstation',
            name='address',
            field=models.CharField(default=None, max_length=255, unique=True),
        ),
    ]
