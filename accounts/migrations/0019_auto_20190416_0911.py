# Generated by Django 2.1.5 on 2019-04-16 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20190416_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='company_benifits',
            field=models.CharField(blank=True, default='NSSF', max_length=1000),
        ),
    ]
