# Generated by Django 2.1.5 on 2019-03-05 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ACCNTS', '0002_auto_20190304_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='amount',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='invoice',
            name='balance',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
