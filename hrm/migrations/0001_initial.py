# Generated by Django 4.1.4 on 2023-05-05 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CompanyDetail",
            fields=[
                (
                    "systemfield_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.systemfield",
                    ),
                ),
                ("company_name", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("pincode", models.IntegerField()),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
            ],
            bases=("core.systemfield",),
        ),
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "systemfield_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.systemfield",
                    ),
                ),
                (
                    "profile_image",
                    models.ImageField(
                        default="media/defaultprofile.jpeg", upload_to="media/"
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("ADMIN", "Admin"),
                            ("EMPLOYEE", "Employee"),
                            ("GENERAL_USER", "General_User"),
                        ],
                        default="GENERAL_USER",
                        max_length=12,
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=70, null=True)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("MALE", "Male"), ("FEMALE", "female")],
                        max_length=6,
                        null=True,
                    ),
                ),
                ("dob", models.DateField(blank=True, null=True)),
                ("mobile", models.CharField(default="9999999999", max_length=10)),
                ("address", models.CharField(blank=True, max_length=70, null=True)),
                ("pincode", models.IntegerField(default=208023)),
                ("city", models.CharField(blank=True, max_length=70, null=True)),
                ("state", models.CharField(blank=True, max_length=70, null=True)),
                ("department", models.CharField(blank=True, max_length=70, null=True)),
                ("designation", models.CharField(blank=True, max_length=70, null=True)),
                ("about", models.TextField()),
                ("salary", models.IntegerField(blank=True, null=True)),
                (
                    "manager",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hrm.employee",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_employee",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            bases=("core.systemfield",),
        ),
        migrations.CreateModel(
            name="HolidayList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "holiday_name",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("holiday_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="PaySlip",
            fields=[
                (
                    "systemfield_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.systemfield",
                    ),
                ),
                ("payslip_name", models.CharField(max_length=250)),
                ("path", models.FilePathField(max_length=250, path="media")),
                ("dispatch_date", models.DateField()),
                ("salary", models.IntegerField(default=0)),
                ("earning", models.IntegerField(default=0)),
                (
                    "employee_payslip",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="employee_payslip",
                        to="hrm.employee",
                    ),
                ),
            ],
            bases=("core.systemfield",),
        ),
        migrations.CreateModel(
            name="LeaveManagement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("leave_reason", models.TextField()),
                ("leave_days", models.IntegerField()),
                ("leave_start_date", models.DateField()),
                (
                    "leave_type",
                    models.CharField(
                        choices=[("PAID", "Paid"), ("UNPAID", "Unpaid")], max_length=10
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("APPROVED", "Approved"),
                            ("REJECTED", "Rejected"),
                            ("PENDING", "Pending"),
                        ],
                        default="PENDING",
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "employee_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="leaves",
                        to="hrm.employee",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EmployeeBankDetail",
            fields=[
                (
                    "systemfield_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.systemfield",
                    ),
                ),
                ("bank_name", models.CharField(blank=True, max_length=70, null=True)),
                (
                    "account_holder_name",
                    models.CharField(blank=True, max_length=70, null=True),
                ),
                ("branch", models.CharField(blank=True, max_length=70, null=True)),
                (
                    "bank_account_no",
                    models.CharField(blank=True, max_length=70, null=True),
                ),
                ("ifsc_code", models.CharField(blank=True, max_length=70, null=True)),
                ("pan_no", models.CharField(blank=True, max_length=70, null=True)),
                ("pf_no", models.CharField(blank=True, max_length=70, null=True)),
                ("pf_uan", models.CharField(blank=True, max_length=70, null=True)),
                (
                    "employee_bankdetail",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="employee_bank_detail",
                        to="hrm.employee",
                    ),
                ),
            ],
            bases=("core.systemfield",),
        ),
        migrations.CreateModel(
            name="EmployeeManager",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("hrm.employee",),
        ),
    ]
