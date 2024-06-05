# Generated by Django 5.0.6 on 2024-06-05 02:07

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mission', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Waypoint',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('altitude', models.FloatField()),
                ('radius', models.FloatField(default=5)),
                ('pass_radius', models.FloatField(default=5)),
                ('pass_option', models.IntegerField(choices=[(0, 'Passthrough'), (1, 'Orbit Clockwise'), (-1, 'Orbit Counter-Clockwise')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='OrderedWaypoint',
            fields=[
                ('waypoint_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='nav.waypoint')),
                ('order', models.IntegerField()),
            ],
            bases=('nav.waypoint',),
        ),
        migrations.CreateModel(
            name='MissionWaypoint',
            fields=[
                ('orderedwaypoint_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='nav.orderedwaypoint')),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mission.mission')),
            ],
            bases=('nav.orderedwaypoint',),
        ),
    ]
