# Generated by Django 4.0.4 on 2024-09-01 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ilearnsite', '0020_rename_image_url_yourorder_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalquality',
            name='url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='locationbranch',
            name='url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='mustknow',
            name='video_url',
            field=models.FileField(upload_to='static/img'),
        ),
        migrations.AlterField(
            model_name='services',
            name='url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='yourorder',
            name='url',
            field=models.URLField(),
        ),
    ]
