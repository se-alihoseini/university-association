from rest_framework import serializers
from .models import Article, Podcast, Event, Comment, Category, Image
from accounts.models import User


# CommentSerializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('name', 'content', 'created_at')


class UserArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('full_name', 'image')


# ArticleSerializers

class ArchiveArticleSerializer(serializers.ModelSerializer):
    article_user = UserArticleSerializer(source='author')
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Article
        fields = ('title', 'slug', 'image', 'article_user', 'status', 'category')


class CreateArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'en_title', 'content', 'image', 'category')


class RetrieveArticleSerializer(serializers.ModelSerializer):
    comment_article = CommentSerializer(source='comment', many=True)
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Article
        fields = ('author', 'title', 'slug', 'short_description', 'content', 'image', 'category', 'updated_at'
                  , 'comment_article')


# CategorySerializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'id', 'slug')


# PodCastSerializer

class ArchivePodCastSerializer(serializers.ModelSerializer):
    comment_podcast = CommentSerializer(source='comment', many=True)

    class Meta:
        model = Podcast
        fields = ('title', 'slug', 'sound', 'description', 'image', 'speaker', 'data_collector', 'text_editor',
                  'sound_editor', 'graphic_designer', 'comment_podcast', 'id')


class RetrievePodCastSerializer(serializers.ModelSerializer):
    comment_podcast = CommentSerializer(source='comment', many=True)

    class Meta:
        model = Podcast
        fields = ('title', 'slug', 'sound', 'description', 'image', 'speaker', 'data_collector', 'text_editor',
                  'sound_editor', 'graphic_designer', 'comment_podcast', 'id')


# EventSerializer

class ListEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'slug', 'image', 'is_active', 'id')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image',)
        