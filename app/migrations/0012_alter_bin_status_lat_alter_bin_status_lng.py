# Generated by Django 4.1.4 on 2022-12-28 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_bin_status_lat_alter_bin_status_lng'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bin_status',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='bin_status',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
    ]
