# Generated by Django 2.1.5 on 2019-03-08 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0005_auto_20190227_0754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applyleave',
            name='period',
        ),
    ]
