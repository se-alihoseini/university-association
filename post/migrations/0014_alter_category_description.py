# Generated by Django 4.2 on 2023-05-16 11:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_comment_post_slug_comment_post_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
