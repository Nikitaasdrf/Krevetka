# Generated by Django 3.1.7 on 2021-03-17 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0051_auto_20210317_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientinfo',
            name='dateDone',
            field=models.CharField(max_length=25, null=True, verbose_name='Дата выполнения'),
        ),
    ]
