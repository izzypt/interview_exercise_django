# Generated by Django 4.1.6 on 2023-02-09 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findings', '0002_rename_scan_scanmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='findingsmodel',
            name='definition_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='findingsmodel',
            name='target_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='scanmodel',
            name='value',
            field=models.CharField(max_length=100),
        ),
    ]
