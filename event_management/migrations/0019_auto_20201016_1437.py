# Generated by Django 3.1 on 2020-10-16 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0018_auto_20201013_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='ticket_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='event_management.ticket'),
        ),
        migrations.AlterField(
            model_name='batch_ticket',
            name='cus_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='event_management.customer'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='leave_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='salary',
            name='dept_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_management.department'),
        ),
        migrations.AlterField(
            model_name='salary',
            name='emp_det_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_management.emp_details'),
        ),
        migrations.AlterField(
            model_name='salary',
            name='paid',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='salary',
            name='sal_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]