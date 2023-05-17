from post.models import Podcast
from rest_framework.generics import ListAPIView
from home.serializer import HomePodcastSerializer


class PodcastHomeView(ListAPIView):
    authentication_classes = []
    serializer_class = HomePodcastSerializer
    queryset = Podcast.objects.filter(status='p')[:1]
