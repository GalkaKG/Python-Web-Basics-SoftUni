from django.shortcuts import render, redirect

from My_Music_App.web.forms import CreateProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm
from My_Music_App.web.models import Profile, Album


def get_profile():
    return Profile.objects.first()


def get_all_albums():
    return Album.objects.all()


def get_album(pk):
    return Album.objects.get(pk=pk)


def home(request):
    profile = get_profile()
    albums = get_all_albums()

    if profile:
        context = {
            'profile': profile,
            'albums': albums
        }

        return render(request, 'profile/home-with-profile.html', context)

    else:
        if request.method == 'GET':
            form = CreateProfileForm()
        else:
            form = CreateProfileForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('home page')

        context = {
            'profile': profile,
            'form': form
        }

        return render(request, 'profile/home-no-profile.html', context)


def details_profile(request):
    profile = get_profile()
    albums = get_all_albums()

    context = {
        'profile': profile,
        'count_albums': len(albums)
    }

    return render(request, 'profile/profile-details.html', context)


def delete_profile(request):
    profile = get_profile()
    albums = get_all_albums()

    if request.method == 'GET':
        albums.delete()
        profile.delete()
        return redirect('home page')

    return render(request, 'profile/profile-delete.html')


def add_album(request):
    if request.method == 'GET':
        form = CreateAlbumForm()
    else:
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form
    }

    return render(request, 'album/add-album.html', context)


def details_album(request, pk):
    album = get_album(pk)

    context = {
        'album': album
    }

    return render(request, 'album/album-details.html', context)


def edit_album(request, pk):
    album = get_album(pk)

    if request.method == 'GET':
        form = EditAlbumForm(instance=album)
    else:
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')
    context = {
        'album': album,
        'form': form
    }

    return render(request, 'album/edit-album.html', context)


def delete_album(request, pk):
    album = get_album(pk)

    if request.method == 'GET':
        form = DeleteAlbumForm(instance=album)
    else:
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'album': album,
        'form': form
    }

    return render(request, 'album/delete-album.html', context)
