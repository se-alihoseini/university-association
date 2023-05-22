from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from post.models import Article
from post.serializer import ArchiveArticleSerializer


class ArticleProfileView(APIView):

    def get(self, request):
        user = request.user
        queryset = Article.objects.filter(author=user)
        srz_data = ArchiveArticleSerializer(data=queryset, many=True)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)
