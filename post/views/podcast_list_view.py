from rest_framework.generics import ListAPIView
from post.models import Podcast
from post.serializer import ListPodCastSerializer


class PodcastListView(ListAPIView):
    serializer_class = ListPodCastSerializer
    authentication_classes = []
    queryset = Podcast.objects.filter(status='p')
