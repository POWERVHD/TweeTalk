# Generated by Django 5.1.6 on 2025-02-26 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_rename_created_tweet_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='tweets/'),
        ),
    ]
