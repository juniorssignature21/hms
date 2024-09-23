# Generated by Django 5.1 on 2024-09-18 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('advance', 'advance'), ('completed', 'completed'), ('failed', 'Failed'), ('refunded', 'refunded')], default='pending', max_length=20),
        ),
    ]
