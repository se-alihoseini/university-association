from post.models import Article
from rest_framework.generics import ListAPIView
from post.serializer import ArchiveArticleSerializer


class ArticleHomeView(ListAPIView):
    authentication_classes = []
    serializer_class = ArchiveArticleSerializer
    queryset = Article.objects.filter(status='p', is_top=True)[:6]
