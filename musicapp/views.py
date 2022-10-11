from django.shortcuts import render

# Create your views here.

# create a generic view to display all the songs in the database

from rest_framework import generics
from .models import Song, Lyric, Artiste
from .serializers import SongSerializer, LyricSerializer, ArtisteSerializer


class SongListCreateView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


song_list_create = SongListCreateView.as_view()


class SongRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


song_retrieve_update_destroy = SongRetrieveUpdateDestroyView.as_view()


# create a generic view to display all the lyrics in the database


class LyricListCreateView(generics.ListCreateAPIView):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer


lyric_list_create = LyricListCreateView.as_view()


class LyricsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer


lyrics_retrieve_update_destroy = LyricsRetrieveUpdateDestroyView.as_view()

# create a generic view to display all the artistes in the database
class ArtisteListCreateView(generics.ListCreateAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer


artiste_list_create = ArtisteListCreateView.as_view()


class ArtisteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer


artist_retrieve_update_destroy = ArtisteRetrieveUpdateDestroyView.as_view()
