# Generated by Django 4.2 on 2023-07-06 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_alter_course_en_title_alter_course_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='coursevideo',
            name='description',
            field=models.TextField(),
        ),
    ]
