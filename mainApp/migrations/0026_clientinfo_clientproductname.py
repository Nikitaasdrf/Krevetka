# Generated by Django 3.1.7 on 2021-03-13 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0025_auto_20210312_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientinfo',
            name='ClientProductName',
            field=models.CharField(max_length=100, null=True, verbose_name='Заказанные продукты'),
        ),
    ]