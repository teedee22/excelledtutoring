# Generated by Django 2.2.6 on 2019-10-17 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20191008_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blog_post_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]