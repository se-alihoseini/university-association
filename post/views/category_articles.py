from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from post.models import Category, Article
from home.serializer import HomeArticleSerializer


class CategoryArticlesView(APIView):

    def get(self, request, category_slug):
        category = Category.objects.get(slug=category_slug)
        queryset = Article.objects.filter(status='p', category=category)
        srz_data = HomeArticleSerializer(instance=queryset, many=True)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)
