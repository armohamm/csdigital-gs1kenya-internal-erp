# Generated by Django 2.1.5 on 2019-04-23 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ACCNTS', '0022_remove_income_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='income',
            old_name='giver',
            new_name='name',
        ),
    ]
