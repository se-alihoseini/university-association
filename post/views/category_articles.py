from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from post.models import Category, Article
from post.serializer import ArchiveArticleSerializer


class CategoryArticlesView(APIView):
    serializer_class = ArchiveArticleSerializer

    def get(self, request, category_slug):
        category = Category.objects.get(slug=category_slug)
        queryset = Article.objects.filter(status='p', category=category)
        srz_data = ArchiveArticleSerializer(instance=queryset, many=True)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)
