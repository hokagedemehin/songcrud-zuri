from .models import Artiste, Song, Lyric
from rest_framework import serializers


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"


class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = "__all__"
        # depth = 1


class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = "__all__"
