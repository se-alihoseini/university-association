from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from post.models import Article
from post.serializer import ListArticleSerializer, RetrieveArticleSerializer
from mixin import MultipleFieldLookupMixin


class ArticleViewSet(MultipleFieldLookupMixin, ViewSet):
    queryset = Article.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    lookup_field = 'slug'

    def list(self, request):
        queryset = self.queryset.filter(status='p')
        srz_data = ListArticleSerializer(instance=queryset, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)

    def create(self, request):
        user = request.user
        srz_data = ListArticleSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.validated_data['author'] = user
            srz_data.create(srz_data.validated_data)
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, slug=None):
        queryset = get_object_or_404(self.queryset, slug=slug, status='p')
        srz_data = RetrieveArticleSerializer(instance=queryset)
        return Response(srz_data.data, status=status.HTTP_200_OK)

    def partial_update(self, request, slug=None):
        queryset = get_object_or_404(self.queryset, slug=slug)
        srz_data = ListArticleSerializer(instance=queryset, data=request.POST, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, slug=None):
        article = get_object_or_404(self.queryset, slug=slug)
        if article.author == request.user:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
