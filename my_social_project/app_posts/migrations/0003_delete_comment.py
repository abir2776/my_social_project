# Generated by Django 3.2.11 on 2022-08-01 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_posts', '0002_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
