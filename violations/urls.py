from django.urls import path
from django.contrib.auth import views as auth_views

from violations.views import *

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', RegisterView.as_view(), name='register'),
    path('profile/', profile, name='profile'),
    path('allPost/', allPost, name='allPost')
]