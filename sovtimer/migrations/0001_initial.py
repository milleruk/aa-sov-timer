# Generated by Django 3.1.3 on 2020-11-10 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AaSovtimer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name": "Sovereignty Timer",
                "permissions": (
                    ("basic_access", "Can access the Sovereignty Timer module"),
                ),
                "managed": False,
                "default_permissions": (),
            },
        ),
    ]
