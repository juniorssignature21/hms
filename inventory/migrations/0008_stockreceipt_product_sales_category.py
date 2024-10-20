# Generated by Django 5.1 on 2024-10-19 22:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_stockreceipt_product'),
        ('pos', '0002_alter_order_staff_alter_order_waiter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockreceipt',
            name='product_sales_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pos.productcategory'),
        ),
    ]
