# Generated by Django 4.2 on 2023-05-28 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0031_alter_podcast_data_collector_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
