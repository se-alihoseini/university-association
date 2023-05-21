from rest_framework import serializers
from .models import Article, Podcast, Event, Comment


class ListArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'en_title', 'slug', 'short_description', 'content')


class RetrieveArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ListPodCastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = ('title', 'slug', 'image', 'time')


class RetrievePodCastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'


class ListEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'slug', 'image', 'is_active')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('name', 'body')
