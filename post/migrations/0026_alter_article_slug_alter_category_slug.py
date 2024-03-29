# Generated by Django 4.2 on 2023-05-23 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0025_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
