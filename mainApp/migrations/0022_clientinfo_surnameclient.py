# Generated by Django 3.1.2 on 2021-02-20 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0021_clientinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientinfo',
            name='SurnameClient',
            field=models.CharField(max_length=25, null=True, verbose_name='Фамилия клиента'),
        ),
    ]
