# Generated by Django 5.1 on 2024-09-20 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0005_alter_employee_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='address',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='gender',
        ),
    ]
