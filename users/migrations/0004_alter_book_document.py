# Generated by Django 4.2.7 on 2023-11-19 22:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_book_document"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="document",
            field=models.FileField(
                default="default/default.txt", upload_to="documents/"
            ),
        ),
    ]