# Generated by Django 5.1.2 on 2024-10-13 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("quotes", "0002_alter_author_born_location"),
    ]

    operations = [
        migrations.RenameField(
            model_name="quote",
            old_name="tegs",
            new_name="tags",
        ),
    ]
