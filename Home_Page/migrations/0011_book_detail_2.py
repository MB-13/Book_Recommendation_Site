# Generated by Django 5.0.7 on 2024-10-29 10:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Home_Page", "0010_book_detail_weighted_avg"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book_Detail_2",
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
                ("Title", models.CharField(max_length=400)),
                ("Author", models.CharField(max_length=200, null=True)),
                (
                    "Genre",
                    models.CharField(
                        choices=[
                            ("biography", "biography"),
                            ("children", "childrean"),
                            ("fantasy", "fantasy"),
                            ("fiction", "fiction"),
                            ("mystery", "mystery"),
                            ("non-fiction", "non-fiction"),
                            ("romance", "romance"),
                            ("science", "science"),
                            ("science fiction", "science fiction"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                ("Description", models.CharField(max_length=8000, null=True)),
                ("Publish_year", models.CharField(max_length=20, null=True)),
                ("Cover_url", models.CharField(max_length=300, null=True)),
                (
                    "Rating",
                    models.FloatField(
                        default=0,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(5),
                        ],
                    ),
                ),
                (
                    "Rating_Count",
                    models.BigIntegerField(
                        default=0,
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                ("weighted_avg", models.FloatField(null=True)),
            ],
        ),
    ]