# Generated by Django 3.2.11 on 2022-08-01 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_posts', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
