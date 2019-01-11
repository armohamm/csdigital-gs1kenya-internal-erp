# Generated by Django 2.1.5 on 2019-01-10 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
        ('leave', '0009_remove_applyleave_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyleave',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='department', to='departments.Department'),
        ),
    ]
