from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('home', views.home,name = "home"),
    path('forum',views.forum,name = "akforum"),
    path('sign_up/',views.sign_up,name="sign-up"),
    path('naik/',views.naik,name="naik"),
    path('posts/',views.posts,name="posts"),
    path('news/',views.news,name="news"),
    path('register/',views.register,name="register"),
    path('contact/',views.contact,name="contact")
]