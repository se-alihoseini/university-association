from post.models import Event
from post.serializer import FirstEventSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class FirstEventView(APIView):
    serializer_class = FirstEventSerializer

    def get(self, request):
        event = Event.objects.all().first()
        srz_data = FirstEventSerializer(instance=event)
        return Response(srz_data.data, status=status.HTTP_200_OK)
