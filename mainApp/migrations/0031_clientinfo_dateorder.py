# Generated by Django 3.1.7 on 2021-03-15 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0030_auto_20210315_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientinfo',
            name='dateOrder',
            field=models.CharField(max_length=25, null=True, verbose_name='Дата поступлкния'),
        ),
    ]
