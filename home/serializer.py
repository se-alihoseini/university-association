from rest_framework import serializers
from post.models import Article, Podcast, Category
from .models import Slider


class HomeArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'author', 'slug', 'image')


class HomePodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = ('title', 'time', 'speaker', 'image')


class SerializerSlider(serializers.ModelSerializer):
    class Meta:
        model = Slider
        exclude = ('is_active', 'created_at')


class SerializerCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'icon', 'slug')
