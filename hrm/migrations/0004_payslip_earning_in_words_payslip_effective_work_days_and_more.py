# Generated by Django 4.1.4 on 2023-08-02 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0003_payslip_admin_confirmation'),
    ]

    operations = [
        migrations.AddField(
            model_name='payslip',
            name='earning_in_words',
            field=models.CharField(default='Zero', max_length=100),
        ),
        migrations.AddField(
            model_name='payslip',
            name='effective_work_days',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='payslip',
            name='generated_payslip',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='payslip',
            name='loss_pay_days',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='payslip',
            name='salary_month_name',
            field=models.CharField(default='Zero', max_length=20),
        ),
        migrations.AddField(
            model_name='payslip',
            name='total_pay_days',
            field=models.IntegerField(default=0),
        ),
    ]