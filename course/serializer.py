from rest_framework import serializers
from course.models import Course, Teacher, CourseVideo, CourseCategory


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        exclude = ('en_name', 'id')


class CourseVideoSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CourseVideo
        fields = ('name', 'category', 'time', 'video_file')


class CourseVideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseVideo
        fields = ('name', 'slug')


class CourseSerializer(serializers.ModelSerializer):
    course_teacher = TeacherSerializer(source='teacher')

    class Meta:
        model = Course
        fields = ('title', 'slug', 'description', 'date', 'full_time', 'course_teacher')


class RetrieveCourseSerializer(serializers.ModelSerializer):
    course_video = CourseVideoListSerializer('course_video', many=True)

    class Meta:
        model = Course
        fields = ('title', 'slug', 'description', 'date', 'full_time', 'course_video')


class V2CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ('name', 'slug')
