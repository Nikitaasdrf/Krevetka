# Generated by Django 3.1.2 on 2021-02-03 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_auto_20210203_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='fishproduct',
            name='ProductRating',
            field=models.CharField(max_length=50, null=True, verbose_name='Рейтинг'),
        ),
    ]