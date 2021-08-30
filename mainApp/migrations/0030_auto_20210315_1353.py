# Generated by Django 3.1.7 on 2021-03-15 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0029_auto_20210315_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientinfo',
            name='prcount',
            field=models.CharField(max_length=100, null=True, verbose_name='Вес заказа'),
        ),
        migrations.AddField(
            model_name='clientinfo',
            name='prprice',
            field=models.CharField(max_length=100, null=True, verbose_name='Цена заказа'),
        ),
        migrations.AlterField(
            model_name='clientinfo',
            name='prname',
            field=models.CharField(max_length=100, null=True, verbose_name='Название продукта'),
        ),
    ]