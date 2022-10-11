from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("songs/", views.song_list_create, name="song_list_create"),
    path(
        "songs/<int:pk>/",
        views.song_retrieve_update_destroy,
        name="song_retrieve_update_destroy",
    ),
    path("lyrics/", views.lyric_list_create, name="lyric_list_create"),
    path(
        "lyrics/<int:pk>/",
        views.lyrics_retrieve_update_destroy,
        name="lyrics_retrieve_update_destroy",
    ),
    path("artistes/", views.artiste_list_create, name="artiste_list_create"),
    path(
        "artistes/<int:pk>/",
        views.artist_retrieve_update_destroy,
        name="artist_retrieve_update_destroy",
    ),
]
