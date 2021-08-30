# Generated by Django 3.1.5 on 2021-01-30 23:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductBuyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductPicture', models.ImageField(null=True, upload_to=None)),
                ('ProductName', models.CharField(max_length=50, null=True, verbose_name='ProductName')),
                ('ProductPricePer', models.CharField(max_length=50, null=True, verbose_name='ProductPricePer')),
                ('ProductUnitsWanted', models.CharField(max_length=50, null=True, verbose_name='ProductUnitsWanted')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]