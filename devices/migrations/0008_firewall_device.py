# Generated by Django 4.0.4 on 2023-01-25 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0007_firewall_qos_rules_qos_filters'),
    ]

    operations = [
        migrations.AddField(
            model_name='firewall',
            name='device',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='devices.device'),
            preserve_default=False,
        ),
    ]
