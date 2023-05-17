from django.db import models
from post.models import Category
from ckeditor.fields import RichTextField


class CourseVideo(models.Model):
    name = models.CharField(max_length=30)
    en_name = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)
    description = RichTextField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='course_video')
    video_file = models.FileField()
    time = models.TimeField()

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=30)
    en_title = models.CharField(max_length=30)
    slug = models.CharField(max_length=40)
    description = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_course')
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name='teacher_course')
    date = models.DateField()
    full_time = models.TimeField()
    created_at = models.TimeField()
    updated_at = models.TimeField()

    def __str__(self):
        return self.title


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    bio_link = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/teacher/%y /%m /%d')

    def __str__(self):
        return self.name
