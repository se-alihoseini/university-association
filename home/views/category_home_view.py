from post.models import Category
from rest_framework.generics import ListAPIView
from home.serializer import SerializerCategory


class CategoryHomeView(ListAPIView):
    authentication_classes = []
    serializer_class = SerializerCategory
    queryset = Category.objects.filter(in_menu=True)
