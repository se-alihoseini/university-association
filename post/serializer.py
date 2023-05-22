from rest_framework import serializers
from .models import Article, Podcast, Event, Comment, Category
from accounts.models import User


# ArticleSerializers


class UserArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('full_name', 'image')


class ArchiveArticleSerializer(serializers.ModelSerializer):
    article_user = UserArticleSerializer(source='author')

    class Meta:
        model = Article
        fields = ('title', 'slug', 'image', 'article_user', 'status')


class RetrieveArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


# CategorySerializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


# PodCastSerializer

class ArchivePodCastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = ('title', 'slug', 'image', 'time')


class RetrievePodCastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'


# EventSerializer

class ListEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'slug', 'image', 'is_active')


# CommentSerializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('name', 'body')
