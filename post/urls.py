from django.urls import path
from rest_framework import routers
from .views import article_crud_view, podcast_list_view, podcast_retrieve_view, attend_to_event, event_list_view, \
    canceling_event_view, add_comment_view, list_comment_view, category_view, category_articles, upload_image,\
    event_retrieve_view

app_name = 'post'
urlpatterns = [
    path('podcast/archive/', podcast_list_view.PodcastListView.as_view(), name='podcast_archive'),
    path('podcast/<int:id>/<slug:slug>/', podcast_retrieve_view.PodcastRetrieveView.as_view(), name='podcast_retrieve'),
    path('event/archive/', event_list_view.EventListView.as_view(), name='event_archive'),
    path('event/<int:pk>/', event_retrieve_view.EventRetrieveView.as_view(), name='event_retrieve'),
    path('event/attend/<int:event_id>/', attend_to_event.AttendToEvent.as_view(), name='attend_to_event'),
    path('event/canceling/<int:event_id>/', canceling_event_view.CancelingEvent.as_view(), name='event_canceling'),
    path('comment/send/<str:post_type>/<slug:post_slug>/', add_comment_view.AddCommentView.as_view(), name='add_comment'),
    path('comment/list/<str:post_type>/<slug:post_slug>/', list_comment_view.ListCommentView.as_view(), name='list_comment'),
    path('categories/', category_view.CategoryView.as_view(), name='category_view'),
    path('<int:category_id>/articles/', category_articles.CategoryArticlesView.as_view(), name='category_articles'),
    path('image/upload/', upload_image.UploadImage.as_view(), name='upload_image'),
]

router = routers.SimpleRouter()
router.register('article', article_crud_view.ArticleViewSet, basename='article')
urlpatterns += router.urls
