from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/", views.index, name="wiki_index"),
    path("wiki/random", views.random_page, name="random_page"),
    path("wiki/add", views.add_page, name="add_page"),
    path("wiki/<str:page>", views.pages, name="pages"),
    path("wiki/<str:page>/edit", views.edit_page, name="edit_page")
]