# Generated by Django 4.0.6 on 2022-08-18 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='user_img',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='profile_image/'),
        ),
    ]