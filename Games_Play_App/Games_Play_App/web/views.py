from django.shortcuts import render, redirect

from Games_Play_App.web.models import ProfileModel, GameModel
from Games_Play_App.web.forms import CreateProfileForm, CreateGameForm, EditGameForm, DeleteGameForm, EditProfileForm, \
    DeleteProfileForm


def get_profile():
    try:
        return ProfileModel.objects.get()
    except ProfileModel.DoesNotExist:
        return None


def get_all_games():
    return GameModel.objects.all()


def get_game(pk):
    return GameModel.objects.filter(pk=pk).get()


def index(request):
    profile = get_profile()

    context = {
        'profile': profile
    }

    return render(request, 'base/home-page.html', context)


def dashboard(request):
    profile = get_profile()
    games = get_all_games()

    context = {
        'profile': profile,
        'games': games
    }

    return render(request, 'base/dashboard.html', context)


def create_profile(request):
    profile = get_profile()

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

    return render(request, 'profile/create-profile.html', context)


def details_profile(request):
    profile = get_profile()
    games = get_all_games()
    total_rating = 0

    for game in games:
        total_rating += game.rating

    context = {
        'profile': profile,
        'games': games,
        'avg_rating': total_rating / len(games)
    }

    return render(request, 'profile/details-profile.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
        return redirect('details profile')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    games = get_all_games()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        form.save()
        for game in games:
            deleted_game = DeleteGameForm(request.POST, instance=game)
            deleted_game.save()
        return redirect('home page')

    context = {
        'profile': profile
    }

    return render(request, 'profile/delete-profile.html', context)


def create_game(request):
    if request.method == 'GET':
        form = CreateGameForm()
    else:
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, 'game/create-game.html', context)


def details_game(request, pk):
    profile = get_profile()
    game = get_game(pk)

    context = {
        'profile': profile,
        'game': game
    }

    return render(request, 'game/details-game.html', context)


def edit_game(request, pk):
    profile = get_profile()
    game = get_game(pk)

    if request.method == 'GET':
        form = EditGameForm(instance=game)
    else:
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
        return redirect('dashboard')

    context = {
        'game': game,
        'form': form
    }

    return render(request, 'game/edit-game.html', context)


def delete_game(request, pk):
    game = get_game(pk)

    if request.method == 'GET':
        form = DeleteGameForm(instance=game)
    else:
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
        return redirect('dashboard')

    context = {
        'game': game,
        'form': form
    }

    return render(request, 'game/delete-game.html', context)
