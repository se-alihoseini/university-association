# Generated by Django 4.2 on 2023-05-16 08:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_slider_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
