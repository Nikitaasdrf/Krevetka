# Generated by Django 3.1.7 on 2021-03-17 10:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0038_auto_20210317_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientinfo',
            name='dateDone',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 17, 13, 29, 21, 438593), null=True, verbose_name='Дата выполнения'),
        ),
    ]