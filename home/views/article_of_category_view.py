from post.models import Article, Category
from rest_framework.views import APIView
from home.serializer import HomeArticleSerializer, SerializerCategory
from rest_framework.response import Response
from rest_framework import status


class ArticleOfCategoryView(APIView):
    authentication_classes = []
    serializer_class = HomeArticleSerializer

    def get(self, request, category_slug):
        queryset = Category.objects.get(slug=category_slug)
        article = queryset.category_article.filter(status='p')
        srz_data = HomeArticleSerializer(instance=article, many=True)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)
