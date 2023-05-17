# Generated by Django 4.2 on 2023-05-16 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='image/article/%y /%m /%d'),
        ),
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(upload_to='image/category/%y /%m /%d'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='image/event/%y /%m /%d'),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='image',
            field=models.ImageField(upload_to='image/podcast/%y /%m /%d'),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='sound',
            field=models.FileField(upload_to='sound/podcast/%y /%m /%d'),
        ),
    ]
