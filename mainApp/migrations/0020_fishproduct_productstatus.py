# Generated by Django 3.1.2 on 2021-02-15 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0019_auto_20210215_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='fishproduct',
            name='ProductStatus',
            field=models.CharField(max_length=25, null=True, verbose_name='Статус'),
        ),
    ]
