# Generated by Django 3.1.7 on 2021-03-17 11:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0046_auto_20210317_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientinfo',
            name='dateDone',
            field=models.DateField(default=datetime.datetime(2021, 3, 20, 14, 0, 25, 958157), verbose_name='Дата выполнения'),
        ),
    ]
