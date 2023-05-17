from rest_framework.generics import RetrieveAPIView
from post.models import Podcast
from post.serializer import RetrievePodCastSerializer
from mixin import MultipleFieldLookupMixin


class PodcastRetrieveView(MultipleFieldLookupMixin, RetrieveAPIView):
    serializer_class = RetrievePodCastSerializer
    authentication_classes = []
    queryset = Podcast.objects.filter(status='p')
    lookup_fields = ['id', 'slug']
