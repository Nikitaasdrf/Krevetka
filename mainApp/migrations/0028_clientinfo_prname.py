# Generated by Django 3.1.7 on 2021-03-15 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0027_clientinfo_clientproductcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientinfo',
            name='prname',
            field=models.CharField(max_length=100, null=True, verbose_name='Название2'),
        ),
    ]