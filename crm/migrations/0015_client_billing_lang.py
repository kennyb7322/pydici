# Generated by Django 2.2.13 on 2020-12-13 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0014_auto_20201212_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='billing_lang',
            field=models.CharField(choices=[('fr-fr', 'French'), ('en-en', 'English')], default='fr-fr', max_length=10, verbose_name='Language'),
        ),
    ]