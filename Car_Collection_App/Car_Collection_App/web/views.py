from django.shortcuts import render, redirect
from Car_Collection_App.web.forms import CreateProfileForm, CreateCarForm, EditCarForm, DeleteCarForm, EditProfileForm
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
    profile = get_profile()
    cars = get_all_cars()

    context = {
        'profile': profile,
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
    profile = get_profile()
    cars = get_all_cars()

    total_price_all_cars = sum([car.price for car in cars])

    context = {
        'profile': profile,
        'all_cars_sum': total_price_all_cars
    }

    return render(request, 'profile/profile-details.html', context)


def profile_edit(request):
    profile = get_profile()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'profile/profile-edit.html', context)


def profile_delete(request):
    if request.method == 'POST':
        get_all_cars().delete()
        get_profile().delete()
        return redirect('home')

    return render(request, 'profile/profile-delete.html')


def car_create(request):
    profile = get_profile()

    if request.method == 'GET':
        form = CreateCarForm()
    else:
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'car/car-create.html', context)


def car_details(request, pk):
    profile = get_profile()
    car = get_car(pk)

    context = {
        'profile': profile,
        'car': car
    }

    return render(request, 'car/car-details.html', context)


def car_edit(request, pk):
    profile = get_profile()
    car = get_car(pk)

    if request.method == 'GET':
        form = EditCarForm(instance=car)
    else:
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'car': car,
        'form': form
    }

    return render(request, 'car/car-edit.html', context)


def car_delete(request, pk):
    profile = get_profile()
    car = get_car(pk)

    if request.method == 'GET':
        form = DeleteCarForm(instance=car)
    else:
        form = DeleteCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
        return redirect('catalogue')

    context = {
        'profile': profile,
        'car': car,
        'form': form
    }

    return render(request, 'car/car-delete.html', context)
