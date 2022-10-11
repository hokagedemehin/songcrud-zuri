from asyncio.windows_events import NULL
from django.db import models

# Create your models here.


class Artiste(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.first_name


class Song(models.Model):
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    date_released = models.DateField(null=True, blank=True)
    likes = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title


class Lyric(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE, null=True)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.content
