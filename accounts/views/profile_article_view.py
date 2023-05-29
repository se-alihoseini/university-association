from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from post.models import Article
from post.serializer import ArchiveArticleSerializer


class ArticleProfileView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ArchiveArticleSerializer

    def get(self, request):
        user = request.user.id
        queryset = Article.objects.filter(author=user)
        srz_data = ArchiveArticleSerializer(instance=queryset, many=True)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)
