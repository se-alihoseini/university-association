from rest_framework.generics import ListAPIView
from course.models import Course
from course.serializer import CourseSerializer


class CourseListView(ListAPIView):
    serializer_class = CourseSerializer
    authentication_classes = []
    queryset = Course.objects.all()
