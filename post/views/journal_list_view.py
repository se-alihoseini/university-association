from rest_framework.generics import ListAPIView
from post.models import Journal
from post.serializer import JournalSerializer


class JournalListView(ListAPIView):
    serializer_class = JournalSerializer
    authentication_classes = []
    queryset = Journal.objects.all()
