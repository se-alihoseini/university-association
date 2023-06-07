from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from accounts.models import User


class Article(models.Model):
    Status_Choice = (
        ('p', 'published'),
        ('d', 'draft'),
        ('t', 'trash'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_article')
    title = models.CharField(max_length=50)
    en_title = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, null=True, blank=True)
    content = RichTextField()
    image = models.ImageField(blank=True, null=True, upload_to='image/article/%y /%m /%d')
    status = models.CharField(max_length=1, choices=Status_Choice, default='d')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category_article')
    comment = models.ManyToManyField('Comment', related_name='comment_article', blank=True)
    is_top = models.BooleanField(default=False)
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.en_title)
        super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-created_at',)


class Podcast(models.Model):
    Status_Choice = (
        ('p', 'published'),
        ('d', 'draft'),
        ('t', 'trash'),
    )
    title = models.CharField(max_length=50)
    en_title = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, null=True, blank=True)
    time = models.TimeField()
    sound = models.FileField(upload_to='sound/podcast/%y /%m /%d')
    description = RichTextField()
    image = models.ImageField(upload_to='image/podcast/%y /%m /%d')
    speaker = models.CharField(max_length=30)
    data_collector = models.CharField(max_length=50)
    text_editor = models.CharField(max_length=30)
    sound_editor = models.CharField(max_length=30)
    graphic_designer = models.CharField(max_length=30)
    status = models.CharField(max_length=1, choices=Status_Choice, default='d')
    comment = models.ManyToManyField('Comment', related_name='comment_podcast', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)


class Event(models.Model):
    title = models.CharField(max_length=50)
    en_title = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='image/event/%y /%m /%d')
    content = RichTextField()
    users = models.ManyToManyField(User, related_name='user_event', blank=True)
    date = models.DateField()
    expire_time = models.DateField()
    is_active = models.BooleanField(default=False)
    time = models.TimeField()
    place = models.CharField(max_length=50)
    provider = models.CharField(max_length=50)
    max_user = models.IntegerField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.en_title)
        super(Event, self).save(*args, **kwargs)

    def user_count(self):
        return self.users.count()

    def user_list(self):
        queryset = list(self.users.values_list('email', flat=True, ))
        return "\n".join(queryset)

    class Meta:
        ordering = ('-date',)


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    en_name = models.CharField(max_length=20, unique=True)
    slug = models.CharField(max_length=20, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    # icon = models.ImageField(upload_to='image/category/%y /%m /%d')
    # is_sub = models.BooleanField()
    in_menu = models.BooleanField(default=False)
    # parent = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.en_name)
        super(Category, self).save(*args, **kwargs)


class Comment(models.Model):
    Status_Choice = (
        ('a', 'accepted'),
        ('w', 'waiting'),
    )
    Type = (
        ('a', 'article'),
        ('p', 'podcast'),
    )
    name = models.CharField(max_length=20, null=True)
    # article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_comment')
    content = models.TextField(max_length=400)
    post_type = models.CharField(max_length=1, choices=Type, null=True)
    post_slug = models.SlugField(null=True)
    status = models.CharField(max_length=1, choices=Status_Choice, default='w')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.content[:15]}'


class Image(models.Model):
    image = models.ImageField(upload_to='image/user_upload/%y /%m /%d')


class Journal(models.Model):
    image = models.ImageField(upload_to='image/Journal/%y /%m /%d')
    title = models.CharField(max_length=30)
    src = models.FileField(upload_to='file/Journal/%y /%m /%d')

    def __str__(self):
        return self.title
