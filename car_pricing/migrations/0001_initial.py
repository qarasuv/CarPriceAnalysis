# Generated by Django 5.1.3 on 2024-11-13 16:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='img/logos/')),
                ('url', models.URLField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('url', models.URLField(max_length=255)),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='car_pricing.make')),
            ],
        ),
        migrations.CreateModel(
            name='Generation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/generations/')),
                ('url', models.URLField(max_length=255)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='generations', to='car_pricing.model')),
            ],
        ),
    ]
