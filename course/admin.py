from django.contrib import admin
from django.contrib.admin import StackedInline
from .models import Course, CourseVideo, Teacher


class CourseVideoAdmin(StackedInline):
    model = CourseVideo
    extra = 1
    prepopulated_fields = {'slug': ('en_name',)}


class CourserAdmin(admin.ModelAdmin):
    list_display = ('title', 'en_title', 'teacher', 'date', 'full_time')
    prepopulated_fields = {'slug': ('en_title',)}
    inlines = [CourseVideoAdmin, ]


admin.site.register(Course, CourserAdmin)

admin.site.register(Teacher)