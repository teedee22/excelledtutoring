# Generated by Django 2.2.6 on 2019-10-08 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_ourteam'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='team_intro_large_text',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='team_intro_small_text',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
