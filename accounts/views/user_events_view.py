from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from post.serializer import ListEventSerializer
from post.models import Event


class UserEventsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        events = Event.objects.filter(users=user)
        srz_data = ListEventSerializer(instance=events, many=True)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)