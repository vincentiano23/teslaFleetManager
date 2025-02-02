# Generated by Django 5.1.2 on 2024-11-03 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicle_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telemetry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('speed', models.DecimalField(decimal_places=2, max_digits=5)),
                ('location', models.CharField(max_length=100)),
                ('efficiency', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telemetry', to='vehicle_data.vehicle')),
            ],
        ),
    ]
