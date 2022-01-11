from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs', views.blogs, name='blog'),
    path('about', views.about, name='about'),
]
