
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", views.globalD, name="tracks"),
    path("nation/", views.Track, name="track"),
    path("news/", views.News, name="news"),
    path("district-wise/", views.DistrictWise, name="district"),
    path("manifest.json/",TemplateView.as_view(template_name="manifest.json", content_type="application/json"),name="manifest.json",),
]
