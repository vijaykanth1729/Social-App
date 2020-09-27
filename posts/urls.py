
from django.urls import path
from .views import all_posts, post_like_or_unlike

app_name = 'posts'
urlpatterns  = [

    path('posts/', all_posts, name='all-posts'),
    path('liked/', post_like_or_unlike, name='like-post-view')
]
