# Generated by Django 2.2.6 on 2019-10-07 16:46

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_banner_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageTestimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('testimonial_text', models.CharField(blank=True, max_length=700, null=True)),
                ('testimonial_author', models.CharField(blank=True, max_length=200, null=True)),
                ('testimonial_location', models.CharField(blank=True, max_length=100, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='testimonials', to='home.HomePage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
