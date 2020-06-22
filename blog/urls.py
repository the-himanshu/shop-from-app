from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="BlogHome"),
    path("blogpost/<int:ordid>", views.blogpost, name="BlogPost"),
    path("search/", views.search, name="BlogSearch"),
    path("makePost/", views.makePost, name="MakePost"),
    path("savePost/", views.savePost, name="SavePost"),
]

