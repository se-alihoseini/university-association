from rest_framework.generics import ListAPIView
from post.models import Podcast
from post.serializer import ArchivePodCastSerializer


class PodcastListView(ListAPIView):
    serializer_class = ArchivePodCastSerializer
    authentication_classes = []
    queryset = Podcast.objects.filter(status='p')
