# Generated by Django 4.2.1 on 2023-05-27 22:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test0", "0003_alter_user_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_id",
            field=models.CharField(
                max_length=14,
                primary_key=True,
                serialize=False,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[0-9]{14,14}$",
                        message="Enter valid Egyptian national identity number",
                    )
                ],
            ),
        ),
    ]
