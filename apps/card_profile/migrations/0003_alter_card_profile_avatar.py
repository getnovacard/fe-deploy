# Generated by Django 3.2.7 on 2021-10-01 16:07

import apps.card_profile.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card_profile', '0002_alter_card_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card_profile',
            name='avatar',
            field=models.ImageField(max_length=255, upload_to=apps.card_profile.models.Card_profile.path_and_rename),
        ),
    ]
