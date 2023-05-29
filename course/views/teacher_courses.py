from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from course.models import Course, Teacher
from course.serializer import CourseSerializer, TeacherSerializer
from django.shortcuts import get_object_or_404


class TeacherCoursesView(APIView):
    authentication_classes = []
    lookup_field = 'slug'
    serializer_class = CourseSerializer

    def get(self, request, teacher_slug):
        teacher = get_object_or_404(Teacher, slug=teacher_slug)
        courses = Course.objects.filter(teacher=teacher)
        srz_data = CourseSerializer(instance=courses, many=True)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)
