from django.urls import path

from . import views

app_name = 'enc'

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.page, name='page'), 
    path("search/", views.search, name='search'),
    path("create_page/", views.create_page, name="create"),
    path("wiki/<str:title>/edit/", views.edit, name="edit"),
    path("random/", views.random_page, name="random"),
]
