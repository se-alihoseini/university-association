from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from post.models import Comment
from post.serializer import CommentSerializer


class ListCommentView(APIView):
    authentication_classes = []
    serializer_class = CommentSerializer

    def get(self, request, post_type, post_slug):
        comments = Comment.objects.filter(post_slug=post_slug, post_type=post_type, status__exact='a')
        srz_data = CommentSerializer(instance=comments, many=True)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)
