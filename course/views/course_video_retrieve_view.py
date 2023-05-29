from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from course.models import CourseVideo, Course
from course.serializer import CourseVideoSerializer
from django.shortcuts import get_object_or_404


class CourseVideoRetrieveView(APIView):
    authentication_classes = []
    lookup_field = 'slug'
    serializer_class = CourseVideoSerializer

    def get(self, request, course_video_slug):
        video = CourseVideo.objects.get(slug=course_video_slug)
        srz_data = CourseVideoSerializer(instance=video)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)
