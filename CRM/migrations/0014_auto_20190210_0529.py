# Generated by Django 2.1.5 on 2019-02-10 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0013_auto_20190210_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barcode',
            name='GTIN',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
