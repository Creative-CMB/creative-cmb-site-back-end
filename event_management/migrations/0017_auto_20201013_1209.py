# Generated by Django 3.0.8 on 2020-10-13 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0016_auto_20201013_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created_month',
            field=models.CharField(max_length=5),
        ),
    ]