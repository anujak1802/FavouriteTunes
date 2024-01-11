
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('songs/', views.song_list, name='song_list'),
    path('songs/<int:song_id>/', views.song_detail, name='song_detail'),
    path('add_song/', views.add_song, name='add_song'),
    path('add_artist/', views.add_artist, name='add_artist'),
    path('artist_song_count/', views.artist_song_count, name='artist_song_count'),
    path('delete_song/<int:song_id>/', views.delete_song, name='delete_song'),
    path('edit_song/<int:song_id>/', views.edit_song, name='edit_song'),
]
