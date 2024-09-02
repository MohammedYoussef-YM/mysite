# Generated by Django 4.1.7 on 2023-07-24 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ilearnsite', '0002_aboutskills_contact_aboutus_image_cover_page_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutskills',
            old_name='skill_title',
            new_name='skill_title_en',
        ),
        migrations.RenameField(
            model_name='aboutus',
            old_name='description',
            new_name='description2_en',
        ),
        migrations.RenameField(
            model_name='aboutus',
            old_name='description2',
            new_name='description_en',
        ),
        migrations.RenameField(
            model_name='aboutus',
            old_name='title',
            new_name='title_en',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='description',
            new_name='description_en',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='title_en',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='office',
            new_name='office_en',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='description',
            new_name='description_en',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='teacher',
            new_name='teacher_en',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='title',
            new_name='title_en',
        ),
        migrations.RenameField(
            model_name='opnion',
            old_name='big_description',
            new_name='big_description_en',
        ),
        migrations.RenameField(
            model_name='opnion',
            old_name='little_description',
            new_name='little_description_en',
        ),
        migrations.RenameField(
            model_name='opnion',
            old_name='title',
            new_name='title_en',
        ),
        migrations.RenameField(
            model_name='partners',
            old_name='description',
            new_name='description_en',
        ),
        migrations.RenameField(
            model_name='partners',
            old_name='title',
            new_name='title_en',
        ),
        migrations.RenameField(
            model_name='slide',
            old_name='description',
            new_name='description_en',
        ),
        migrations.RenameField(
            model_name='slide',
            old_name='title',
            new_name='title_en',
        ),
        migrations.RenameField(
            model_name='values',
            old_name='description',
            new_name='description_en',
        ),
        migrations.RenameField(
            model_name='values',
            old_name='title',
            new_name='title_en',
        ),
    ]
