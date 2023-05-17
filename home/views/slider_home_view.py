from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from home.models import Slider
from home.serializer import SerializerSlider
from django.shortcuts import get_object_or_404


class SliderView(APIView):
    authentication_classes = []

    def get(self, request):
        queryset = get_object_or_404(Slider, is_active=True)
        srz_data = SerializerSlider(instance=queryset, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)