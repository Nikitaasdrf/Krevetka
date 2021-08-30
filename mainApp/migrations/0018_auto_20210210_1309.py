# Generated by Django 3.1.2 on 2021-02-10 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0017_auto_20210210_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='infonikita',
            name='NikitaID',
            field=models.CharField(max_length=50, null=True, verbose_name='ProductID'),
        ),
        migrations.AlterField(
            model_name='infonikita',
            name='NikitaName',
            field=models.CharField(max_length=25, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='infonikita',
            name='NikitaProfil',
            field=models.CharField(max_length=25, null=True, verbose_name='Характеристика'),
        ),
    ]
