# Generated by Django 4.0.4 on 2023-01-08 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0003_rename_id_device_device_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='ip',
            field=models.CharField(default='10.0.0.1', max_length=30),
        ),
        migrations.AddField(
            model_name='device',
            name='wifi_pwd',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='wifi_ssid',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='device',
            name='name',
            field=models.CharField(blank=True, default='RPI', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='type',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.CreateModel(
            name='Telemetry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('timestamp', models.CharField(max_length=30)),
                ('data', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.device')),
            ],
        ),
    ]