# Generated by Django 4.2.1 on 2023-05-29 12:33

import Games_Play_App.web.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('category', models.CharField(choices=[('ACTION', 'Action'), ('ADVENTURE', 'Adventure'), ('PUZZLE', 'Puzzle'), ('STRATEGY', 'Strategy'), ('SPORTS', 'Sports'), ('BOARD/CARD GAME', 'Board/Card Game'), ('OTHER', 'Other')], max_length=15)),
                ('rating', models.FloatField(validators=[Games_Play_App.web.models.rating_validate])),
                ('max_level', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('image_url', models.URLField()),
                ('summary', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(12)])),
                ('password', models.CharField(max_length=30)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
