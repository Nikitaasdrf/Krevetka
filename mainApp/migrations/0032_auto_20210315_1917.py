# Generated by Django 3.1.7 on 2021-03-15 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0031_clientinfo_dateorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientinfo',
            name='dateOrder',
            field=models.CharField(max_length=25, null=True, verbose_name='Дата поступления'),
        ),
    ]
