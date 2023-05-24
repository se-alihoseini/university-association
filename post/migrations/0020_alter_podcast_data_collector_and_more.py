# Generated by Django 4.2 on 2023-05-22 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0019_alter_event_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='data_collector',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='graphic_designer',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='sound_editor',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='speaker',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='text_editor',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]