# Generated by Django 5.1.3 on 2025-01-01 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lectures2025", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="llibre",
            name="llib_lector",
        ),
        migrations.RemoveField(
            model_name="llibre",
            name="llib_propietari",
        ),
    ]
