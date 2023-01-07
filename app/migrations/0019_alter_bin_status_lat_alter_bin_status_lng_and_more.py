# Generated by Django 4.1.4 on 2023-01-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_bin_status_lat_alter_bin_status_lng_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bin_status',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='bin_status',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='camera_vision',
            name='loc_lat',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='camera_vision',
            name='loc_lng',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True, unique=True),
        ),
    ]
