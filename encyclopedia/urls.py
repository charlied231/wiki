from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>/", views.title, name ="title"),
    path("search", views.search, name="search"),
    path("newpage", views.newPage, name="newPage"),
    path('editpage', views.editPage, name="editPage"),
    path('randpage', views.randPage, name="randPage"),

]
