# Generated by Django 5.2 on 2025-04-21 10:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0011_remove_about_available_for_freelance_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Skill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("projects_completed", models.PositiveIntegerField()),
                (
                    "starting_price",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("icon_svg", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
