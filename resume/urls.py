
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index_page, name="base"),
    path("about/", views.about, name="about-section"),
]
