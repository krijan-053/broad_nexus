# Generated by Django 4.2.3 on 2023-07-14 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0003_userprofile"),
    ]

    operations = [
        migrations.RenameField(
            model_name="userprofile",
            old_name="addrdess",
            new_name="address",
        ),
    ]