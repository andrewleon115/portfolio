# Generated by Django 5.2 on 2025-04-19 04:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0010_about_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="about",
            name="available_for_freelance",
        ),
        migrations.RemoveField(
            model_name="about",
            name="location",
        ),
        migrations.RemoveField(
            model_name="about",
            name="name",
        ),
    ]
