# Generated by Django 4.2 on 2023-07-06 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_slider_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
