# Generated by Django 4.1.4 on 2022-12-30 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_rename_location1_lat_camera_vision_loc1_lat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera_vision',
            name='loc1status',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='camera_vision',
            name='loc2status',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='camera_vision',
            name='loc3status',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='camera_vision',
            name='loc4status',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
