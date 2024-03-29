from django.urls import path
from rest_framework import routers
from .views import article_crud_view, podcast_list_view, podcast_retrieve_view, attend_to_event, event_list_view, \
    canceling_event_view, add_comment_view, list_comment_view, category_view, category_articles, upload_image,\
    event_retrieve_view, journal_list_view, edit_article_content_view, first_event_view

app_name = 'post'
urlpatterns = [
    path('podcast/archive/', podcast_list_view.PodcastListView.as_view(), name='podcast_archive'),
    path('podcast/<int:id>/<slug:slug>/', podcast_retrieve_view.PodcastRetrieveView.as_view(), name='podcast_retrieve'),
    path('journal/archive/', journal_list_view.JournalListView.as_view(), name='journal_archive'),
    path('event/archive/', event_list_view.EventListView.as_view(), name='event_archive'),
    path('event/first/', first_event_view.FirstEventView.as_view(), name='first_event'),
    path('event/<slug:slug>/', event_retrieve_view.EventRetrieveView.as_view(), name='event_retrieve'),
    path('event/attend/<int:event_id>/', attend_to_event.AttendToEvent.as_view(), name='attend_to_event'),
    path('event/canceling/<int:event_id>/', canceling_event_view.CancelingEvent.as_view(), name='event_canceling'),
    path('comment/send/<str:post_type>/<slug:post_slug>/', add_comment_view.AddCommentView.as_view(), name='add_comment'),
    path('comment/list/<str:post_type>/<slug:post_slug>/', list_comment_view.ListCommentView.as_view(), name='list_comment'),
    path('categories/', category_view.CategoryView.as_view(), name='category_view'),
    path('<slug:category_slug>/articles/', category_articles.CategoryArticlesView.as_view(), name='category_articles'),
    path('image/upload/', upload_image.UploadImage.as_view(), name='upload_image'),
    path('article/<slug:slug>/edit/', edit_article_content_view.EditArticleContentView.as_view(), name='edit_article_content_view'),

]

router = routers.SimpleRouter()
router.register('article', article_crud_view.ArticleViewSet, basename='article')
urlpatterns += router.urls
