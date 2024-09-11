# Generated by Django 5.1 on 2024-09-05 23:57

import django.db.models.deletion
import django.utils.timezone
import shortuuid.django_fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0011_room_floor'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='advance_amount',
            new_name='total_amount',
        ),
        migrations.RenameField(
            model_name='coupon',
            old_name='date',
            new_name='date_created',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='arrival_from',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='before_discount',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='booking_type',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='checked_in_tracker',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='checked_out_tracker',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='coupons',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='discount_amount',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='discount_type',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='email',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='payment_mode',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='payment_status',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='saved',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='stripe_payment_intent',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='success_id',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='total',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='total_days',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='vip',
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='make_public',
        ),
        migrations.AddField(
            model_name='booking',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookings.coupon'),
        ),
        migrations.AddField(
            model_name='booking',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coupon',
            name='max_redemptions',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coupon',
            name='type',
            field=models.CharField(choices=[('Percentage', 'Percentage'), ('Fixed', 'Fixed')], default='Percentage', max_length=100),
        ),
        migrations.CreateModel(
            name='AdditionalCharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('minibar', 'Minibar'), ('room_service', 'Room Service'), ('damage', 'Damage'), ('laundry', 'Laundry'), ('other', 'Other')], max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additional_charges', to='bookings.booking')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed'), ('refunded', 'Refunded')], default='pending', max_length=20)),
                ('mode', models.CharField(choices=[('cash', 'Cash'), ('credit_card', 'Credit Card'), ('paypal', 'PayPal')], default='cash', max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('transaction_id', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvxyz', length=10, max_length=20, prefix='', unique=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='bookings.booking')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('num_adults', models.PositiveIntegerField(default=1)),
                ('num_children', models.PositiveIntegerField(default=0)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('reservation_id', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvxyz', length=10, max_length=20, prefix='', unique=True)),
                ('expiration_date', models.DateTimeField(blank=True, null=True)),
                ('is_cancelled', models.BooleanField(default=False)),
                ('cancel_date', models.DateTimeField(blank=True, null=True)),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookings.hotel')),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookings.payment')),
                ('room', models.ManyToManyField(to='bookings.room')),
                ('room_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookings.roomtype')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='booking',
            name='reservation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookings.reservation'),
        ),
    ]
