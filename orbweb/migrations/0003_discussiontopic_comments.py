# Generated by Django 5.0.7 on 2024-07-25 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orbweb', '0002_alter_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussiontopic',
            name='comments',
            field=models.IntegerField(default=0),
        ),
    ]
