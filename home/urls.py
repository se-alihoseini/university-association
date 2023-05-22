from django.urls import path
from rest_framework import routers
# from .views import ArticleHomeView, PodcastHomeView
from home.views.article_home_view import ArticleHomeView
from home.views.podcast_home_view import PodcastHomeView
from home.views.slider_home_view import SliderView

app_name = 'home'
urlpatterns = [
    path('list_article_view/', ArticleHomeView.as_view(), name='list_article_view'),
    path('list_podcast_view/', PodcastHomeView.as_view(), name='list_podcast_view'),
    path('slider_view/', SliderView.as_view(), name='slider_view'),
]
