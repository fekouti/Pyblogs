# Generated by Django 4.0.6 on 2022-08-20 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0005_post_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
