# Generated by Django 3.2.7 on 2021-10-01 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card_profile',
            name='avatar',
            field=models.ImageField(upload_to='uploads/<django.db.models.fields.CharField>'),
        ),
    ]
