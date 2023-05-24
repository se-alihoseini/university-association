# Generated by Django 4.2 on 2023-05-23 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0027_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='en_name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='en_title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]