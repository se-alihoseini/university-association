from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.utils.html import mark_safe


class CourseVideo(models.Model):
    name = models.CharField(max_length=30)
    en_name = models.CharField(max_length=30, unique=True)
    slug = models.CharField(max_length=30)
    description = RichTextField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='course_video')
    video_file = models.FileField()
    time = models.TimeField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.en_name)
        super(CourseVideo, self).save(*args, **kwargs)


class Course(models.Model):
    title = models.CharField(max_length=30)
    en_title = models.CharField(max_length=30, unique=True)
    slug = models.CharField(max_length=40)
    description = RichTextField()
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name='teacher_course')
    date = models.DateField()
    full_time = models.TimeField()
    created_at = models.TimeField()
    updated_at = models.TimeField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.en_title)
        super(Course, self).save(*args, **kwargs)


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    en_name = models.CharField(max_length=30, unique=True)
    slug = models.CharField(max_length=30, blank=True, null=True)
    bio_link = models.URLField()
    image = models.ImageField(upload_to='image/teacher/%y /%m /%d')

    def __str__(self):
        return self.name

    def img_preview(self):
        return mark_safe(f'<img src = "{self.image.url}" width = "80" height="80"/>')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.en_name)
        super(Teacher, self).save(*args, **kwargs)
