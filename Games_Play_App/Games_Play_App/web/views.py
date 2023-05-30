from django.shortcuts import render

from Games_Play_App.web.models import ProfileModel


def get_profile():
    try:
        return ProfileModel.objects.get()
    except ProfileModel.DoesNotExist:
        return None


def index(request):
    profile = get_profile()

    context = {
        'profile': profile
    }
    return render(request, 'base/home-page.html', context)


def dashboard(request):
    return render(request, 'base/dashboard.html')


def create_profile(request):
    return render(request, 'profile/create-profile.html')


def details_profile(request):
    return render(request, 'profile/details-profile.html')


def edit_profile(request):
    return render(request, 'profile/edit-profile.html')


def delete_profile(request):
    return render(request, 'profile/delete-profile.html')


def create_game(request):
    return render(request, 'game/create-game.html')


def details_game(request, pk):
    return render(request, 'game/details-game.html')


def edit_game(request, pk):
    return render(request, 'game/edit-game.html')


def delete_game(request, pk):
    return render(request, 'game/delete-game.html')
