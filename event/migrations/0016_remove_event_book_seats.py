# Generated by Django 4.0.5 on 2022-10-27 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0015_remove_event_participants_booking_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='book_seats',
        ),
    ]
