"""Users URLs."""

# Django
from django.urls import path
# from django.views.generic import TemplateView

# View
from users import views


urlpatterns = [

    # Posts
    path(
        # route='<str:username>/',
        route='profile/<str:username>/',
        # view=TemplateView.as_view(template_name='users/detail.html'),
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

    # Management
    
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='login'
    ),
    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),
    path(
        route='me/profile/',
        view=views.UpdateProfileView.as_view(),
        name='update'
    ),


    path(
        route='signup_view/',
        view=views.signup_view,
        name='signup'
    ),
    path(
        route='login_view/',
        view=views.login_view,
        name='login'
    ),
    path(
        route='logout_view/',
        view=views.logout_view,
        name='logout'
    ),
    path(
        route='me/profile/unused/',
        view=views.update_profile,
        name='update_unused'
    )

]