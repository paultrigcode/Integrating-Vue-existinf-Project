# Generated by Django 3.1.5 on 2021-01-24 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recycle', '0005_auto_20210124_0817'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('agent_percentage', models.FloatField(default=0.0)),
                ('subscriber_percentage', models.FloatField(default=0.0)),
                ('conversion', models.FloatField(default=1)),
                ('collector_can_pickup', models.BooleanField(default=True)),
                ('manager_can_pickup', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pickup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('points_updated', models.BooleanField(blank=True)),
                ('points', models.IntegerField(blank=True, default=0, null=True)),
                ('status', models.CharField(default='Not Sent', max_length=100)),
                ('collector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('recycler', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='recycle.recycler')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('points', models.IntegerField(blank=True, null=True)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='recycle.material')),
                ('pickup', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='recycle.pickup')),
            ],
        ),
    ]
