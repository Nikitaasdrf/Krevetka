# Generated by Django 3.1.7 on 2021-03-17 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0049_auto_20210317_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientinfo',
            name='dateDone',
            field=models.DateField(default='20032021', verbose_name='Дата выполнения'),
        ),
    ]
