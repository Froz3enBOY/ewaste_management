# Generated by Django 4.1.4 on 2022-12-27 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_main_anime_presetlist_delete_known_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('x', 'Male'), ('y', 'Female')], default='', max_length=60, verbose_name='gender')),
            ],
        ),
        migrations.AlterField(
            model_name='main_anime',
            name='category',
            field=models.CharField(choices=[('N', 'notfilled'), ('Y', 'filled')], max_length=2),
        ),
    ]
