from django.contrib import admin
from django.contrib.admin import StackedInline
from course.models import Course, CourseVideo, Teacher, CourseCategory


class CourseVideoAdmin(StackedInline):
    model = CourseVideo
    extra = 1
    prepopulated_fields = {'slug': ('en_name',)}


class CourserAdmin(admin.ModelAdmin):
    list_display = ('title', 'en_title', 'teacher', 'date', 'full_time')
    prepopulated_fields = {'slug': ('en_title',)}
    inlines = [CourseVideoAdmin, ]


admin.site.register(Course, CourserAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'en_name', 'img_preview')
    prepopulated_fields = {'slug': ('en_name',)}
    readonly_fields = ('img_preview',)


admin.site.register(Teacher, TeacherAdmin)


class CourseCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('en_name',)}


admin.site.register(CourseCategory, CourseCategoryAdmin)
