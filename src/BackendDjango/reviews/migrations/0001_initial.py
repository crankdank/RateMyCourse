# Generated by Django 4.0.1 on 2022-01-15 21:19

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('professor', models.CharField(max_length=30)),
                ('semester', models.CharField(max_length=10)),
                ('overall_rate', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('diffculty', models.CharField(blank=True, choices=[('Easy', 'Easy'), ('Moderate Easy', 'Moderate Easy'), ('Medium', 'Medium'), ('Moderate Hard', 'Moderate Hard'), ('Hard', 'Hard')], max_length=14)),
                ('comment', models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]