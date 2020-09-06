# Generated by Django 3.0.6 on 2020-09-06 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0002_admin_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('cus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='event_management.user')),
                ('district', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='event',
            fields=[
                ('event_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('budget', models.FloatField(max_length=5)),
                ('email_address', models.CharField(max_length=50)),
                ('occassion_type', models.CharField(max_length=10)),
                ('eq_quantity', models.IntegerField(max_length=10, null=True)),
                ('time', models.TimeField(auto_now=True)),
                ('head_count', models.IntegerField(max_length=10)),
                ('creator_phone', models.CharField(max_length=10)),
                ('schedule_file', models.CharField(max_length=500)),
                ('date', models.DateField(auto_now=True)),
                ('event_type', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=100)),
                ('event_creator_name', models.CharField(max_length=20)),
                ('eq_list', models.CharField(max_length=500)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_management.user')),
            ],
        ),
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('ticket_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('tkt_name', models.CharField(max_length=50)),
                ('tkt_type', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('price', models.FloatField(default=0.0, max_length=5)),
                ('expiration_date', models.DateField(auto_now=True)),
                ('image', models.CharField(max_length=500)),
                ('no_of_tickets', models.IntegerField(max_length=5)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_management.admin')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_management.event')),
            ],
        ),
        migrations.CreateModel(
            name='package',
            fields=[
                ('pack_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('pack_name', models.CharField(max_length=50)),
                ('featuers', models.CharField(max_length=500)),
                ('pack_type', models.CharField(max_length=100)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_management.admin')),
            ],
        ),
    ]
