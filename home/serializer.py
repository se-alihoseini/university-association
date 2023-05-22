from rest_framework import serializers
from post.models import Article, Podcast, Category
from accounts.models import User
from .models import Slider


class UserArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('full_name', 'image')


class HomeArticleSerializer(serializers.ModelSerializer):
    article_user = UserArticleSerializer(source='author')

    class Meta:
        model = Article
        fields = ('title', 'slug', 'image', 'article_user', 'status')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class HomePodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = ('title', 'time', 'image')


class SerializerSlider(serializers.ModelSerializer):
    class Meta:
        model = Slider
        exclude = ('is_active', 'created_at')


class SerializerCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')
