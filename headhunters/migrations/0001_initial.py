# Generated by Django 5.1.1 on 2024-11-22 09:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("profile_cv", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="StatusAction",
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
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="StatusCandidate",
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
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="TypeAction",
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
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="HeadHunter",
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
                ("company", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=20)),
                (
                    "position",
                    models.CharField(
                        help_text="Position within the company", max_length=100
                    ),
                ),
                (
                    "website",
                    models.URLField(
                        blank=True, help_text="Company website URL", null=True
                    ),
                ),
                (
                    "linkedin_profile",
                    models.URLField(
                        blank=True, help_text="LinkedIn profile URL", null=True
                    ),
                ),
                ("city", models.CharField(max_length=255)),
                ("country", models.CharField(max_length=255)),
                (
                    "profile_photo",
                    models.ImageField(
                        blank=True,
                        help_text="Upload a profile photo",
                        null=True,
                        upload_to="profile_photos/",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="headhunter",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="JobOffer",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("requirements", models.TextField()),
                ("publish_date", models.DateTimeField(auto_now_add=True)),
                (
                    "headhunter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="headhunters.headhunter",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="JobOfferNotification",
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
                ("sent_date", models.DateTimeField(auto_now_add=True)),
                ("read", models.BooleanField(default=False)),
                (
                    "candidate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="profile_cv.profile_cv",
                    ),
                ),
                (
                    "job_offer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="headhunters.joboffer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Schedule",
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
                ("date", models.DateTimeField()),
                (
                    "candidate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="profile_cv.profile_cv",
                    ),
                ),
                (
                    "headhunter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="headhunters.headhunter",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ManagementCandidates",
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
                (
                    "is_selected_by_headhunter",
                    models.BooleanField(
                        default=False,
                        help_text="Indicates if the candidate was selected directly by the headhunter",
                    ),
                ),
                (
                    "applied_directly",
                    models.BooleanField(
                        default=False,
                        help_text="Indicates if the candidate applied to the job offer by themselves",
                    ),
                ),
                ("application_date", models.DateTimeField(auto_now_add=True)),
                (
                    "candidate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="profile_cv.profile_cv",
                    ),
                ),
                (
                    "job_offer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="headhunters.joboffer",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="headhunters.statuscandidate",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Action",
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
                ("description", models.TextField()),
                ("date", models.DateTimeField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "candidate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="profile_cv.profile_cv",
                    ),
                ),
                (
                    "headhunter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="headhunters.headhunter",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="headhunters.statusaction",
                    ),
                ),
                (
                    "type_action",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="headhunters.typeaction",
                    ),
                ),
            ],
        ),
    ]

