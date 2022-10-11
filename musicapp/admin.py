from django.contrib import admin

# Register your models here.

from .models import Song, Lyric, Artiste

admin.site.register(Song)
admin.site.register(Lyric)
admin.site.register(Artiste)
