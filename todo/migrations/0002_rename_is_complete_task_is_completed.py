# Generated by Django 4.1 on 2023-07-22 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task", old_name="is_complete", new_name="is_completed",
        ),
    ]