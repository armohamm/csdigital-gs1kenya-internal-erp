# Generated by Django 2.1.5 on 2019-04-12 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20190412_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='leave_balance',
        ),
    ]
