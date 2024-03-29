# Generated by Django 4.2 on 2023-05-16 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('en_title', models.CharField(max_length=30)),
                ('slug', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('full_time', models.TimeField()),
                ('created_at', models.TimeField()),
                ('updated_at', models.TimeField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_course', to='post.category')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('bio_link', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='teacher/%y /%m /%d')),
            ],
        ),
        migrations.CreateModel(
            name='CourseVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('en_name', models.CharField(max_length=30)),
                ('slug', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('video_file', models.FileField(upload_to='')),
                ('time', models.TimeField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_video', to='course.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_course', to='course.teacher'),
        ),
    ]
