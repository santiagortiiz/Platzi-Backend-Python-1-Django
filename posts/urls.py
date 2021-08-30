"""Posts URLs."""

# Django
from django.urls import path

# Views
from posts import views

urlpatterns = [

    path(
        route='new_post/',
        view=views.create_post,
        name='create'
    ),
    path(
        route='posts',
        view=views.list_posts,
        name='feed_unused'
    ),
    
    path(
        route='new/',
        view=views.CreatePostView.as_view(),
        name='create'
    ),
    path(
        route='',
        view=views.PostsFeedView.as_view(),
        name='feed'
    ),
    path(
        route='posts/<int:pk>/',
        view=views.PostDetailView.as_view(),
        name='detail'
    ),
]