from django.db import models
from ckeditor.fields import RichTextField


class Slider(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='image/slider/%y /%m /%d')
    description = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', )
