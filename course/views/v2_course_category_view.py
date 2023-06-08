from rest_framework.generics import ListAPIView
from course.models import CourseCategory
from course.serializer import V2CourseCategorySerializer


class CourseCategoryView(ListAPIView):
    serializer_class = V2CourseCategorySerializer
    authentication_classes = []
    queryset = CourseCategory.objects.all()
