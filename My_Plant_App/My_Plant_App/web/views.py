from django.shortcuts import render, redirect

from My_Plant_App.web.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm,\
    CreatePlantForm, EditPlantForm, DeletePlantForm
from My_Plant_App.web.models import ProfileModel, PlantModel


def get_profile():
    try:
        return ProfileModel.objects.get()
    except ProfileModel.DoesNotExist:
        return None


def get_plants():
    return PlantModel.objects.all()


def get_plant(pk):
    return PlantModel.objects.filter(pk=pk).get()


def index(request):
    profile = get_profile()

    context = {
        'profile': profile
    }
    return render(request, 'base/home-page.html', context)


def catalogue(request):
    profile = get_profile()
    plants = get_plants()

    context = {
        'profile': profile,
        'plants': plants
    }

    return render(request, 'base/catalogue.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form
    }

    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    profile = get_profile()
    plants = get_plants()

    context = {
        'profile': profile,
        'plants': plants,
        'stars': len(plants)
    }
    return render(request, 'profile/profile-details.html', context)


def profile_edit(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
        return redirect('profile details')

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()
    plants = get_plants()

    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST, instance=profile)
        form.save()
        for plant in plants:
            plant_form = DeletePlantForm(request.POST, instance=plant)
            plant_form.save()

        return redirect('home')

    context = {
        'profile': profile,
    }

    return render(request, 'profile/delete-profile.html', context)


def plant_create(request):
    if request.method == 'GET':
        form = CreatePlantForm()
    else:
        form = CreatePlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form
    }

    return render(request, 'plant/create-plant.html', context)


def plant_details(request, pk):
    profile = get_profile()
    plant = get_plant(pk)

    context = {
        'profile': profile,
        'plant': plant
    }
    return render(request, 'plant/plant-details.html', context)


def plant_edit(request, pk):
    profile = get_profile()
    plant = get_plant(pk)

    if request.method == 'GET':
        form = EditPlantForm(instance=plant)
    else:
        form = EditPlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'plant': plant,
        'form': form
    }

    return render(request, 'plant/edit-plant.html', context)


def plant_delete(request, pk):
    profile = get_profile()
    plant = get_plant(pk)

    if request.method == 'GET':
        form = DeletePlantForm(instance=plant)
    else:
        form = DeletePlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'plant': plant,
        'form': form
    }

    return render(request, 'plant/delete-plant.html', context)
