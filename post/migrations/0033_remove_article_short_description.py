# Generated by Django 4.2 on 2023-06-05 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0032_article_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='short_description',
        ),
    ]
