# Generated by Django 2.2.13 on 2021-01-16 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffing', '0011_auto_20200302_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='management_mode',
            field=models.CharField(choices=[('LIMITED', 'Limité'), ('ELASTIC', 'Élastique'), ('NONE', 'Aucun')], default='NONE', max_length=30, verbose_name='Management mode'),
        ),
    ]