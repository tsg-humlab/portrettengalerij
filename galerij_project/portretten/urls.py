from django.urls import path
from . import views

app_name = 'portretten'
urlpatterns = [
    path("", views.index, name="index"),
    path("objects/", views.objects, name="objects"),
]