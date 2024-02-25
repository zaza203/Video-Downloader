from django.urls import path
from .views import *
from . import views

urlpatterns =[
    path("", views.home, name = 'home'),
    path("get-videos", views.get_video, name = "get_video"),
    path("<str:arg>", views.download_video, name="download_video"),
    # path('get-playlist', views.get_playlist, name='get_playlist'),
]