from django.shortcuts import render, redirect

from My_Music_App.web.forms import CreateProfileForm, CreateAlbumForm
from My_Music_App.web.models import Profile, Album


def get_profile():
    return Profile.objects.first()


def get_all_albums():
    return Album.objects.all()


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
    return render(request, 'profile/profile-details.html')


def delete_profile(request):
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
    return render(request, 'album/album-details.html')


def edit_album(request, pk):
    return render(request, 'album/edit-album.html')


def delete_album(request, pk):
    return render(request, 'album/delete-album.html')
