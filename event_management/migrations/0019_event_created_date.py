# Generated by Django 3.0.8 on 2020-10-13 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0018_auto_20201013_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='created_date',
            field=models.CharField(default='2020-10-13 07:59:39', max_length=20),
        ),
    ]
