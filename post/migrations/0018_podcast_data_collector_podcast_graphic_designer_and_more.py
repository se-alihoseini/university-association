# Generated by Django 4.2 on 2023-05-21 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0017_remove_category_icon_remove_category_is_sub_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='data_collector',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='podcast',
            name='graphic_designer',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='podcast',
            name='sound_editor',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='podcast',
            name='speaker',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='podcast',
            name='text_editor',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
