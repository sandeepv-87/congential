from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('signup/', views.user_signup,name='signup'),
    path('login/', views.user_login,name='login'),
]
