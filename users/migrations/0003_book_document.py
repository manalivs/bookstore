# Generated by Django 4.2.7 on 2023-11-19 21:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_rename_newusers_book_rename_username_book_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="document",
            field=models.FileField(null=True, upload_to=""),
        ),
    ]