"""platzigram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Django Core
from django.contrib import admin
from django.urls import path, include

# Allow to serve media in development environment
from django.conf import settings
from django.conf.urls.static import static 

# Models
from platzigram import views as local_views
from posts import views as posts_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', local_views.hello_world),
    path('access/<str:name>/<int:age>/', local_views.access),

    path('posts/', posts_views.list_posts, name='feed'),
    path('posts_test/', posts_views.list_posts_test),
    path('template_testing/', posts_views.template_testing),

    path('', posts_views.list_posts, name='feed'),
    path('posts/new/', posts_views.create_post, name='create_post'),

    path('users/signup/', user_views.signup_view, name='signup'),
    path('users/login/', user_views.login_view, name='login'),
    path('users/logout/', user_views.logout_view, name='logout'),
    path('users/me/profile', user_views.update_profile, name='update_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
