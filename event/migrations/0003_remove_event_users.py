# Generated by Django 4.0.5 on 2022-10-25 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_event_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='users',
        ),
    ]
