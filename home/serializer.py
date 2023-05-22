from rest_framework import serializers
from post.models import Article, Podcast, Category
from accounts.models import User
from .models import Slider


class SerializerSlider(serializers.ModelSerializer):
    class Meta:
        model = Slider
        exclude = ('is_active', 'created_at')
