# Generated by Django 5.1 on 2024-10-16 13:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0002_employee_role_delete_employeerole'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockreceipt',
            name='department_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hrm.employee'),
        ),
    ]
