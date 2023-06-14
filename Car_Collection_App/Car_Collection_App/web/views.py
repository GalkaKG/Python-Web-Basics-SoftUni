from django.shortcuts import render, redirect

from Car_Collection_App.web.forms import CreateProfileForm, CreateCarForm
from Car_Collection_App.web.models import Profile, Car


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def get_car(pk):
    return Car.objects.get(pk=pk)


def get_all_cars():
    return Car.objects.all()


def index(request):
    profile = get_profile()

    context = {
        'profile': profile
    }

    return render(request, 'base/index.html', context)


def catalogue(request):
    cars = get_all_cars()

    context = {
        'cars': cars
    }

    return render(request, 'base/catalogue.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form
    }

    return render(request, 'profile/profile-create.html', context)


def profile_details(request):
    return render(request, 'profile/profile-details.html')


def profile_edit(request):
    return render(request, 'profile/profile-edit.html')


def profile_delete(request):
    return render(request, 'profile/profile-delete.html')


def car_create(request):
    if request.method == 'GET':
        form = CreateCarForm()
    else:
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form
    }

    return render(request, 'car/car-create.html', context)


def car_details(request, pk):
    car = get_car(pk)

    context = {
        'car': car
    }

    return render(request, 'car/car-details.html', context)


def car_edit(request, pk):
    return render(request, 'car/car-edit.html')


def car_delete(request):
    return render(request, 'car/car-delete.html')
