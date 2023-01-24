# Generated by Django 4.1.5 on 2023-01-24 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EnergyProvider', '0003_bss_isactive'),
        ('ChargingStation', '0007_remove_chargingstation_activedso'),
    ]

    operations = [
        migrations.AddField(
            model_name='chargingstation',
            name='activeDso',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, related_name='active_dso', to='EnergyProvider.dso'),
        ),
    ]
