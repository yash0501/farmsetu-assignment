from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("get_weather/", views.get_weather, name="get_weather"),
]
