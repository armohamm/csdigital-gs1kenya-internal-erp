# Generated by Django 2.1.5 on 2019-01-25 11:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0004_auto_20190125_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='created_on',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
