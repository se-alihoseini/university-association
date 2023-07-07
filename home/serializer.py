from .models import Slider
from rest_framework import serializers


class SerializerSlider(serializers.ModelSerializer):
    class Meta:
        model = Slider
        exclude = ('is_active', 'created_at')


class ContactUsSerializer(serializers.Serializer):
    subject = serializers.CharField()
    email = serializers.EmailField()
    context = serializers.CharField()
