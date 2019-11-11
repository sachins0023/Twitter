from twitter_app.views import *
from django.urls import path


app_name = 'twitter_app'

urlpatterns = [
    path('user/', api_user_list_view, name='user_list'),
    path('tweet/', api_tweet_list_view, name='tweet_list'),
    path('user/<int:id>/', api_user_id_list_view, name='user_id_list'),
    path('tweet/<int:id>/', api_tweet_id_list_view, name='tweet_id_list'),
    path('user/create/',api_create_user_view, name='user_create_list'),
    path('tweet/create/',api_create_tweet_view, name='tweet_create_list'),
    path('tweet/<int:id>/update/', api_update_tweet_view, name='tweet_update_list'),
]
