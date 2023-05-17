from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from post.models import Article, Podcast
from post.serializer import CommentSerializer


class AddCommentView(APIView):
    authentication_classes = []

    def post(self, request, post_type, post_slug):
        srz_data = CommentSerializer(data=request.data)
        if srz_data.is_valid():
            if post_type == 'article':
                srz_data.validated_data['post_type'] = 'a'
                srz_data.validated_data['post_slug'] = post_slug
                comment = srz_data.create(srz_data.validated_data)
                article = get_object_or_404(Article, slug=post_slug)
                article.comment.add(comment)
                return Response(data='ok dawsh article', status=status.HTTP_200_OK)

            elif post_type == 'podcast':
                srz_data.validated_data['post_type'] = 'p'
                srz_data.validated_data['post_slug'] = post_slug
                comment = srz_data.create(srz_data.validated_data)
                podcast = get_object_or_404(Podcast, slug=post_slug)
                podcast.comment.add(comment)
                return Response(data='ok dawsh podcast', status=status.HTTP_200_OK)

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
