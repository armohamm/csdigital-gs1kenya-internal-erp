# Generated by Django 2.1.3 on 2018-12-10 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=14)),
                ('huduma', models.CharField(max_length =50, default = "HUD-001232")),
                ('id_no', models.IntegerField(default = 0)),
                ('nssf_no',  models.CharField(default = "NSSF_NO", max_length=50)),
                ('nhif_no', models.CharField(default = "NHIF_NO", max_length=50)),
                ('KRA', models.CharField(default="KRA_PIN", max_length=30)),
                ('employee_no', models.CharField(default = 'GS1_NO', max_length =50)),
                ('bank', models.IntegerField( default = 123456)),
                ('date_of_birth', models.CharField(max_length=20)),
                ('next_of_kin_name', models.CharField(blank=True, max_length=60)),
                ('kin_email', models.CharField(blank=True, max_length=100)),
                ('county', models.CharField(blank=True, max_length=100)),
                ('next_of_kin_phone', models.CharField(blank=True, max_length=20)),
                ('dependant_name', models.CharField(blank=True, max_length=100)),
                ('dependant_relationship', models.CharField(blank=True, max_length=60)),
                ('dependant_contact', models.CharField(blank=True, max_length=60)),
                ('salary', models.CharField(blank=True, max_length=100)),
                ('department', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='departments.Department')),
                ('position', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='departments.Position')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
