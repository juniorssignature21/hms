# Generated by Django 5.1 on 2024-09-26 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0011_rename_department_employee_department_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emergency_contact_phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]