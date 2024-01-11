from django.shortcuts import render, redirect,get_object_or_404
from .models import Song, Artist
from .forms import SongForm, ArtistForm

def home(request):
    return render(request, 'home.html')

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'song_list.html', {'songs': songs})

def song_detail(request, song_id):
    song = Song.objects.get(id=song_id)
    return render(request, 'song_detail.html', {'song': song})

def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongForm()
    return render(request, 'add_song.html', {'form': form})

def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = ArtistForm()
    return render(request, 'add_artist.html', {'form': form})

def artist_song_count(request):
    artists = Artist.objects.all()
    return render(request, 'artist_song_count.html', {'artists': artists})


def delete_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if request.method == 'POST':
        song.delete()
        return redirect('song_list')
    return render(request, 'delete_song.html', {'song': song})

def edit_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongForm(instance=song)
    return render(request, 'edit_song.html', {'form': form, 'song': song})
