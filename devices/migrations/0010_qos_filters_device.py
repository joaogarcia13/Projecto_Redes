# Generated by Django 4.0.4 on 2023-01-30 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0009_qos_filters_filterhandle_qos_filters_filtertype_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='qos_filters',
            name='device',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='devices.device'),
            preserve_default=False,
        ),
    ]