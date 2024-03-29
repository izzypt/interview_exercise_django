# Generated by Django 4.1.6 on 2023-02-10 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findings', '0003_alter_findingsmodel_definition_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='findingsmodel',
            name='method',
            field=models.CharField(choices=[('GET', 'GET'), ('POST', 'POST'), ('PUT', 'PUT'), ('PATCH', 'PATCH'), ('DELETE', 'DELETE')], max_length=10),
        ),
        migrations.AlterField(
            model_name='findingsmodel',
            name='url',
            field=models.URLField(max_length=1000),
        ),
    ]
