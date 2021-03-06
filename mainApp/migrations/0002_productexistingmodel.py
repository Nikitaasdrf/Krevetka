# Generated by Django 3.1.5 on 2021-01-30 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductExistingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductPicture', models.ImageField(null=True, upload_to='static/imgmodels')),
                ('ProductName', models.CharField(max_length=50, null=True, verbose_name='ProductName')),
                ('ProductPricePer', models.CharField(max_length=50, null=True, verbose_name='ProductPricePer')),
                ('ProductUnitsWanted', models.CharField(max_length=50, null=True, verbose_name='ProductUnitsWanted')),
            ],
        ),
    ]
