# Generated by Django 2.2.6 on 2019-10-08 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20191007_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='blog_featured_large_text',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='blog_featured_small_text',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
