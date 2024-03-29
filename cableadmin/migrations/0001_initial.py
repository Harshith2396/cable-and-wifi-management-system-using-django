# Generated by Django 2.2.6 on 2019-11-24 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='area',
            fields=[
                ('area_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name_of_place', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='cable_properties',
            fields=[
                ('cable_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('cable_plane_name', models.CharField(max_length=30)),
                ('cable_price', models.CharField(max_length=30)),
                ('bandwidth', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='collectors',
            fields=[
                ('collector_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('collector_name', models.CharField(max_length=5)),
                ('area_id', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='customers',
            fields=[
                ('customer_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=30)),
                ('area_id', models.CharField(max_length=5)),
                ('server_id', models.CharField(max_length=5)),
                ('wifi_plans', models.CharField(max_length=5)),
                ('cable_plans', models.CharField(max_length=5)),
                ('subscription_for', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('manager_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('manager_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Servers',
            fields=[
                ('server_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('area_id', models.CharField(max_length=5)),
                ('manager_id', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='wifi_properties',
            fields=[
                ('wifi_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('wifi_plan_name', models.CharField(max_length=30)),
                ('wifi_price', models.CharField(max_length=10)),
                ('speed_provided', models.CharField(max_length=10)),
            ],
        ),
    ]
