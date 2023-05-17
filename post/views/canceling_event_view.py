from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from post.models import Event


class CancelingEvent(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, event_id):
        user = request.user
        event = get_object_or_404(Event, pk=event_id, is_active=True)

        if event.users.filter(id=user.id).exists():
            event.users.remove(user)
            return Response(data='You have canceled the event', status=status.HTTP_200_OK)
        else:
            return Response(data='You are not registered for the event', status=status.HTTP_400_BAD_REQUEST)
