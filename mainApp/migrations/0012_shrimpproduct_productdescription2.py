# Generated by Django 3.1.2 on 2021-02-03 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0011_fishproduct_productdescription2'),
    ]

    operations = [
        migrations.AddField(
            model_name='shrimpproduct',
            name='ProductDescription2',
            field=models.CharField(max_length=35, null=True, verbose_name='Описание товара'),
        ),
    ]
