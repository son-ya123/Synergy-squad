# Generated by Django 4.2.6 on 2023-10-19 05:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("offshelf_app", "0007_alter_iteminfo_image_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="iteminfo",
            name="user",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]