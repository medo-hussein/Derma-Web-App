# Generated by Django 4.2.1 on 2023-05-27 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test0", "0005_user_superuser"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="superuser",),
        migrations.AlterField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
    ]
