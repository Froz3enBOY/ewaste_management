# Generated by Django 4.1.4 on 2023-01-26 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_arduino_fill_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arduino',
            name='check_filled',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.bin_status', unique=True, verbose_name='check_filled'),
        ),
    ]
