# Generated by Django 4.1.4 on 2022-12-28 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_bin_status_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bin_status',
            name='lat',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bin_status',
            name='lng',
            field=models.BigIntegerField(),
        ),
    ]
