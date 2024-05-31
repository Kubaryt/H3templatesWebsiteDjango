# Generated by Django 5.0.6 on 2024-05-31 13:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="OriginalTemplate",
            fields=[
                (
                    "template_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.template",
                    ),
                ),
                ("main_author", models.CharField(max_length=255)),
                ("other_authors", models.TextField()),
            ],
            bases=("core.template",),
        ),
        migrations.CreateModel(
            name="OriginalTemplateRelease",
            fields=[
                (
                    "templaterelease_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.templaterelease",
                    ),
                ),
                (
                    "template",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="original_templates.originaltemplate",
                    ),
                ),
            ],
            bases=("core.templaterelease",),
        ),
    ]