from rest_framework.generics import ListAPIView
from course.models import Teacher
from course.serializer import TeacherSerializer


class TeacherListView(ListAPIView):
    serializer_class = TeacherSerializer
    authentication_classes = []
    queryset = Teacher.objects.all()
