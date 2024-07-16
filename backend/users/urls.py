from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeDoneView,
)
from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path(
        '',
        login_required(views.ListUserView.as_view()),
        name='index'
    ),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login',
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout',
    ),
    path(
        'signup/',
        views.SignUp.as_view(),
        name='signup',
    ),
    path(
        'password_change/',
        views.PasswordChange.as_view(),
        name='password_change',
    ),
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html'
        ),
        name='password_change_done',
    ),
    path(
        'edit/',
        login_required(views.UserView.as_view()),
        name='edit_user'
    ),
    path(
        'delete/',
        login_required(views.delete),
        name='delete_user'
    ),
]
