# Generated by Django 4.2 on 2023-05-16 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(upload_to='image/teacher/%y /%m /%d'),
        ),
    ]
