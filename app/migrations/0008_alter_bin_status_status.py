# Generated by Django 4.1.4 on 2022-12-28 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bin_status',
            name='status',
            field=models.CharField(max_length=60),
        ),
    ]
