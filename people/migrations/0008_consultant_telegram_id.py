# Generated by Django 2.2.13 on 2021-01-30 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_consultant_telegram_alias'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultant',
            name='telegram_id',
            field=models.IntegerField(null=True),
        ),
    ]