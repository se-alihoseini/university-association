from rest_framework.generics import RetrieveAPIView
from post.models import Event
from post.serializer import RetrieveEventSerializer


class EventRetrieveView(RetrieveAPIView):
    serializer_class = RetrieveEventSerializer
    authentication_classes = []
    queryset = Event.objects.all()
