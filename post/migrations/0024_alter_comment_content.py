# Generated by Django 4.2 on 2023-05-22 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0023_alter_comment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=400),
        ),
    ]
