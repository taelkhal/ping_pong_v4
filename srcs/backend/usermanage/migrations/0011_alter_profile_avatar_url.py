# Generated by Django 4.2 on 2025-02-22 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanage', '0010_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar_url',
            field=models.URLField(blank=True, default='/media/avatars/Profile_avatar_placeholder_large.png', max_length=500),
        ),
    ]
