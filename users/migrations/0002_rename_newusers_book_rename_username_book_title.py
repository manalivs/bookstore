# Generated by Django 4.2.7 on 2023-11-19 03:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="newUsers",
            new_name="Book",
        ),
        migrations.RenameField(
            model_name="book",
            old_name="username",
            new_name="title",
        ),
    ]
