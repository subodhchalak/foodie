# Generated by Django 5.0.1 on 2024-01-07 08:14

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=150, null=True)),
                ("last_name", models.CharField(blank=True, max_length=150)),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, unique=True
                    ),
                ),
                (
                    "is_admin",
                    models.BooleanField(default=False, verbose_name="admin status"),
                ),
                (
                    "is_superadmin",
                    models.BooleanField(
                        default=False, verbose_name="superadmin status"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(default=False, verbose_name="staff status"),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="active")),
                ("phone_number", models.CharField(max_length=10)),
                (
                    "role",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("restaurant", "Restaurant"),
                            ("customer", "Customer"),
                        ],
                        max_length=10,
                        null=True,
                        verbose_name="Role",
                    ),
                ),
                (
                    "last_login",
                    models.DateTimeField(auto_now=True, verbose_name="Last Login"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]