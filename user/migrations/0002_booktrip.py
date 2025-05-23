# Generated by Django 4.2.20 on 2025-03-25 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_view', '0002_alter_trip_trip_type'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookTrip',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('guid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_view.tourguide')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_view.trip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user_db')),
            ],
        ),
    ]
