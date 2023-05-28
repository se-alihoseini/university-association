from rest_framework.generics import ListAPIView
from course.models import Teacher
from course.serializer import TeacherSerializer


class TeacherListView(ListAPIView):
    authentication_classes = []
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
