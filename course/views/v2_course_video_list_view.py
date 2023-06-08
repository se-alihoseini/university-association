from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from course.models import CourseCategory, CourseVideo
from course.serializer import CourseVideoSerializer


class V2CourseVideoView(APIView):
    serializer_class = CourseVideoSerializer
    authentication_classes = []

    def get(self, request, category_slug):
        category = CourseCategory.objects.get(slug=category_slug)
        queryset = CourseVideo.objects.filter(category=category)
        srz_data = CourseVideoSerializer(instance=queryset, many=True)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)
