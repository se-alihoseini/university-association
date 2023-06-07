from rest_framework import serializers
from .models import Article, Podcast, Event, Comment, Category, Image, Journal
from accounts.models import User


# CategorySerializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'id', 'slug', 'en_name')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('name', 'content', 'created_at', 'id')


# CommentSerializer
class UserArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('full_name', 'image')


# ArticleSerializers

class ArchiveArticleSerializer(serializers.ModelSerializer):
    article_user = UserArticleSerializer(source='author')
    article_category = CategorySerializer(source='category')

    class Meta:
        model = Article
        fields = ('title', 'slug', 'image', 'article_user', 'status', 'count', 'article_category')


class CreateArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'en_title', 'content', 'image', 'category')


class RetrieveArticleSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Article
        fields = ('author', 'title', 'slug', 'content', 'image', 'category', 'updated_at')


# PodCastSerializer
class ArchivePodCastSerializer(serializers.ModelSerializer):

    class Meta:
        model = Podcast
        fields = ('title', 'slug', 'sound', 'description', 'image', 'speaker', 'data_collector', 'text_editor',
                  'sound_editor', 'graphic_designer', 'id')


class RetrievePodCastSerializer(serializers.ModelSerializer):

    class Meta:
        model = Podcast
        fields = ('title', 'slug', 'sound', 'description', 'image', 'speaker', 'data_collector', 'text_editor',
                  'sound_editor', 'graphic_designer', 'id')


# EventSerializer

class ListEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'slug', 'image', 'is_active', 'id')


class RetrieveEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ('max_user', 'users')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image',)


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'
