from rest_framework.generics import ListAPIView
from post.models import Event
from post.serializer import ListEventSerializer


class EventListView(ListAPIView):
    serializer_class = ListEventSerializer
    authentication_classes = []
    queryset = Event.objects.filter(is_active=True)
