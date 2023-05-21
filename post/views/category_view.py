from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from post.models import Category
from home.serializer import CategorySerializer


class CategoryView(APIView):

    def get(self, request):
        queryset = Category.objects.filter(in_menu=True)
        srz_data = CategorySerializer(instance=queryset, many=True)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)
