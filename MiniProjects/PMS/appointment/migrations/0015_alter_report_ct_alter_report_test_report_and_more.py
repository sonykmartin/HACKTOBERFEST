# Generated by Django 4.0.6 on 2022-08-29 05:33

import appointment.models
from django.db import migrations, models
import functools


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0014_alter_report_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='ct',
            field=models.FileField(blank=True, null=True, upload_to=functools.partial(appointment.models.path_and_rename, *(), **{'field_name': 'ct', 'upload_to': 'files/ct'})),
        ),
        migrations.AlterField(
            model_name='report',
            name='test_report',
            field=models.FileField(blank=True, null=True, upload_to=functools.partial(appointment.models.path_and_rename, *(), **{'field_name': 'report', 'upload_to': 'files/report'})),
        ),
        migrations.AlterField(
            model_name='report',
            name='xray',
            field=models.FileField(blank=True, null=True, upload_to=functools.partial(appointment.models.path_and_rename, *(), **{'field_name': 'xray', 'upload_to': 'files/xray'})),
        ),
    ]
