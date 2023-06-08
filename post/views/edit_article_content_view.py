from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from post.serializer import CreateArticleSerializer
from post.models import Article


class EditArticleContentView(RetrieveAPIView):
    serializer_class = CreateArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Article.objects.all()
    lookup_field = 'slug'
