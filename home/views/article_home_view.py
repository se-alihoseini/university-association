from post.models import Article
from rest_framework.generics import ListAPIView
from home.serializer import HomeArticleSerializer


class ArticleHomeView(ListAPIView):
    authentication_classes = []
    serializer_class = HomeArticleSerializer
    queryset = Article.objects.filter(status='p', is_top=True)[:6]
