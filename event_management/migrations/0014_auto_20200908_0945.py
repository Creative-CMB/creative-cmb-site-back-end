# Generated by Django 3.0.8 on 2020-09-08 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0013_event_event_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='eq_list',
        ),
        migrations.RemoveField(
            model_name='event',
            name='eq_quantity',
        ),
    ]