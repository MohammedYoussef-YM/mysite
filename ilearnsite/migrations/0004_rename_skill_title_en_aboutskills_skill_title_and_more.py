# Generated by Django 4.1.7 on 2023-07-24 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ilearnsite', '0003_rename_skill_title_aboutskills_skill_title_en_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutskills',
            old_name='skill_title_en',
            new_name='skill_title',
        ),
        migrations.RenameField(
            model_name='aboutus',
            old_name='description2_en',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='aboutus',
            old_name='description_en',
            new_name='description2',
        ),
        migrations.RenameField(
            model_name='aboutus',
            old_name='title_en',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='description_en',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='title_en',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='office_en',
            new_name='office',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='description_en',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='teacher_en',
            new_name='teacher',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='title_en',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='opnion',
            old_name='big_description_en',
            new_name='big_description',
        ),
        migrations.RenameField(
            model_name='opnion',
            old_name='little_description_en',
            new_name='little_description',
        ),
        migrations.RenameField(
            model_name='opnion',
            old_name='title_en',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='partners',
            old_name='description_en',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='partners',
            old_name='title_en',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='slide',
            old_name='description_en',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='slide',
            old_name='title_en',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='values',
            old_name='description_en',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='values',
            name='title_en',
        ),
        migrations.AddField(
            model_name='values',
            name='title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
