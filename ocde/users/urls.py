from os import name
from django.urls import path

from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('subscribe/', views.subscribe, name='subscribe'),
]