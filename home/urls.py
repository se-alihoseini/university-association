from django.urls import path
from rest_framework import routers
# from .views import ArticleHomeView, PodcastHomeView
from home.views.article_home_view import ArticleHomeView
from home.views.podcast_home_view import PodcastHomeView
from home.views.slider_home_view import SliderView
from home.views.category_home_view import CategoryHomeView
from home.views.article_of_category_view import ArticleOfCategoryView

app_name = 'post'
urlpatterns = [
    path('list_article_view/', ArticleHomeView.as_view(), name='list_article_view'),
    path('list_podcast_view/', PodcastHomeView.as_view(), name='list_podcast_view'),
    path('slider_view/', SliderView.as_view(), name='slider_view'),
    path('list_category/', CategoryHomeView.as_view(), name='list_category'),
    path('article_of_category/<slug:category_slug>/', ArticleOfCategoryView.as_view(), name='article_of_category'),
]
