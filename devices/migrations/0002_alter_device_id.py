# Generated by Django 4.0.4 on 2022-12-14 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
