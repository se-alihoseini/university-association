from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from post.models import Article
from home.serializer import HomeArticleSerializer


class ArticleProfileView(APIView):

    def get(self, request):
        user = request.user
        queryset = Article.objects.filter(status='p')[:6]
        srz_data = HomeArticleSerializer(data=queryset, many=True)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)
