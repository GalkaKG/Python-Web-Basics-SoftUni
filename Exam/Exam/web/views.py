from django.shortcuts import render, redirect

from Exam.web.forms import CreateProfileForm, CreateFruitForm, EditFruitForm, DeleteFruitForm, EditProfileForm
from Exam.web.models import ProfileModel, FruitModel


def get_profile():
    return ProfileModel.objects.first()


def get_all_fruits():
    return FruitModel.objects.all()


def get_fruit(pk):
    return FruitModel.objects.get(pk=pk)


def index(request):
    profile = get_profile()

    context = {
        'profile': profile
    }

    return render(request, 'base/index.html', context)


def dashboard(request):
    profile = get_profile()
    fruits = get_all_fruits()

    context = {
        'profile': profile,
        'fruits': fruits
    }

    return render(request, 'base/dashboard.html', context)


def create_fruit(request):
    profile = get_profile()

    if request.method == 'GET':
        form = CreateFruitForm()
    else:
        form = CreateFruitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'fruit/create-fruit.html', context)


def details_fruit(request, pk):
    profile = get_profile()
    fruit = get_fruit(pk)

    context = {
        'profile': profile,
        'fruit': fruit
    }

    return render(request, 'fruit/details-fruit.html', context)


def edit_fruit(request, pk):
    profile = get_profile()
    fruit = get_fruit(pk)

    if request.method == 'GET':
        form = EditFruitForm(instance=fruit)
    else:
        form = EditFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'fruit/edit-fruit.html', context)


def delete_fruit(request, pk):
    profile = get_profile()
    fruit = get_fruit(pk)

    if request.method == 'GET':
        form = DeleteFruitForm(instance=fruit)
    else:
        form = DeleteFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            fruit.delete()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'fruit/delete-fruit.html', context)


def create_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'profile/create-profile.html', context)


def details_profile(request):
    profile = get_profile()
    fruits_count = len(get_all_fruits())

    context = {
        'profile': profile,
        'posts': fruits_count
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
    fruits = get_all_fruits()

    if request.POST:
        fruits.delete()
        profile.delete()
        return redirect('home')

    context = {
        'profile': profile
    }

    return render(request, 'profile/delete-profile.html', context)

