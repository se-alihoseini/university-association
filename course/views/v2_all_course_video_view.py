from rest_framework.generics import ListAPIView
from course.models import CourseVideo
from course.serializer import CourseVideoSerializer


class AllCourseVideoListView(ListAPIView):
    authentication_classes = []
    serializer_class = CourseVideoSerializer
    queryset = CourseVideo.objects.all()
