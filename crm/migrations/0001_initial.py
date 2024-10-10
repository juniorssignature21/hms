# Generated by Django 5.1 on 2024-10-08 12:34

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bookings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('target_audience', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_spent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bookings_count', models.PositiveIntegerField(default=0)),
                ('avg_booking_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GuestLifetimeValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_revenue', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lifetime_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('guest', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GuestPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferred_bed_type', models.CharField(blank=True, choices=[('single', 'Single'), ('double', 'Double')], max_length=50, null=True)),
                ('preferred_view', models.CharField(blank=True, choices=[('sea', 'Sea View'), ('city', 'City View')], max_length=50, null=True)),
                ('room_floor_preference', models.CharField(blank=True, choices=[('low', 'Low Floor'), ('high', 'High Floor')], max_length=50, null=True)),
                ('other_preferences', models.TextField(blank=True, null=True)),
                ('guest', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='preferences', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GuestSegment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('guests', models.ManyToManyField(related_name='segments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reward_earned', models.BooleanField(default=False)),
                ('reward_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('referral_date', models.DateField(default=django.utils.timezone.now)),
                ('referred_guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referred_by', to=settings.AUTH_USER_MODEL)),
                ('referrer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referrals', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=255)),
                ('usage_date', models.DateTimeField(auto_now_add=True)),
                ('amount_spent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SpecialRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.TextField()),
                ('fulfilled', models.BooleanField(default=False)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='special_requests', to='bookings.booking')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='special_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_name', models.CharField(max_length=255)),
                ('questions', models.TextField()),
                ('response', models.TextField(blank=True, null=True)),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AbandonedBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('abandonment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('reason', models.TextField(blank=True, null=True)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abandoned_bookings', to=settings.AUTH_USER_MODEL)),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abandoned_bookings', to='bookings.roomtype')),
            ],
            options={
                'indexes': [models.Index(fields=['abandonment_date'], name='crm_abandon_abandon_767f81_idx')],
            },
        ),
        migrations.CreateModel(
            name='GuestFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('comments', models.TextField(blank=True, null=True)),
                ('feedback_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='bookings.booking')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'indexes': [models.Index(fields=['feedback_date'], name='crm_guestfe_feedbac_f5b32c_idx')],
                'unique_together': {('guest', 'booking')},
            },
        ),
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interaction_type', models.CharField(choices=[('email', 'Email'), ('phone', 'Phone'), ('in_person', 'In-Person')], max_length=20)),
                ('interaction_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('notes', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guest_interactions', to=settings.AUTH_USER_MODEL)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_interactions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'indexes': [models.Index(fields=['interaction_date'], name='crm_interac_interac_241720_idx')],
            },
        ),
        migrations.CreateModel(
            name='LoyaltyProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=255)),
                ('transaction_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loyalty_programs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'indexes': [models.Index(fields=['transaction_date'], name='crm_loyalty_transac_d1eb1b_idx')],
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('notification_type', models.CharField(choices=[('email', 'Email'), ('sms', 'SMS')], max_length=50)),
                ('sent_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'indexes': [models.Index(fields=['sent_at'], name='crm_notific_sent_at_773474_idx')],
            },
        ),
        migrations.CreateModel(
            name='ReservationHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('action_type', models.CharField(choices=[('booking', 'Booking'), ('cancellation', 'Cancellation')], max_length=50)),
                ('notes', models.TextField(blank=True, null=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_histories', to='bookings.booking')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_histories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'indexes': [models.Index(fields=['reservation_date'], name='crm_reserva_reserva_3c66d0_idx')],
            },
        ),
        migrations.CreateModel(
            name='RoomPricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(blank=True, max_length=50, null=True)),
                ('demand_factor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pricing', to='bookings.roomtype')),
            ],
            options={
                'indexes': [models.Index(fields=['start_date', 'end_date'], name='crm_roompri_start_d_0e10ef_idx')],
            },
        ),
    ]
