from post.models import Podcast
from rest_framework.generics import ListAPIView
from post.serializer import ArchivePodCastSerializer


class PodcastHomeView(ListAPIView):
    authentication_classes = []
    serializer_class = ArchivePodCastSerializer
    queryset = Podcast.objects.filter(status='p')[:1]
