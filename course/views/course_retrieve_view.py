from rest_framework.generics import RetrieveAPIView
from course.models import Course, CourseVideo
from course.serializer import RetrieveCourseSerializer


class CourseRetrieveView(RetrieveAPIView):
    serializer_class = RetrieveCourseSerializer
    authentication_classes = []
    queryset = Course.objects.all()
    lookup_field = 'slug'
