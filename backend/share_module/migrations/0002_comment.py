# Generated by Django 4.2.7 on 2023-11-08 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("share_module", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("descriptions", models.TextField()),
                (
                    "score",
                    models.CharField(
                        choices=[
                            ("1", "Very Bad"),
                            ("2", "Bad"),
                            ("3", "Normal"),
                            ("4", "Good"),
                            ("5", "Great"),
                        ],
                        max_length=1,
                    ),
                ),
                ("created_datetime", models.DateTimeField(auto_now_add=True)),
                ("demonstrable", models.BooleanField(default=True)),
                ("recommendable", models.BooleanField(default=True)),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="product.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
