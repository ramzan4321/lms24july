# Generated by Django 4.1.4 on 2023-07-24 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0002_leavemanagement_leave_requested_for_payslip_full_day_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payslip',
            name='admin_confirmation',
            field=models.BooleanField(default=False),
        ),
    ]