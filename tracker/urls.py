
from django.urls import path

from . import views

urlpatterns = [
    path("", views.globalD, name="tracks"),
    path("nation/", views.Track, name="track"),
    path("news/", views.News, name="news"),
    path("district-wise/", views.DistrictWise, name="district"),
]
