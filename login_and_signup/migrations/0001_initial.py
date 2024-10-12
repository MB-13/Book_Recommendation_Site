# Generated by Django 5.0.7 on 2024-08-24 17:31

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="userInfo",
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
                ("firstName", models.CharField(max_length=150)),
                ("lastName", models.CharField(max_length=150)),
                ("emailAdderss", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=30)),
            ],
        ),
    ]