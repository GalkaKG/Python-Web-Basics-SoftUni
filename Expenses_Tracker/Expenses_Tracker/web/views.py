from django.shortcuts import render
from Expenses_Tracker.web.models import Profile


def get_profile():
    return Profile.objects.first()


def home(request):
    profile = get_profile()

    if not profile:
        return render(request, 'profile/home-no-profile.html')
    else:
        return render(request, 'profile/home-with-profile.html')


def profile_page(request):
    return render(request, 'profile/profile.html')


def profile_edit(request):
    return render(request, 'profile/profile-edit.html')


def profile_delete(request):
    return render(request, 'profile/profile-delete.html')

def create(request):
    return render(request, 'expense/expense-create.html')


def edit(request, pk):
    return render(request, 'expense/expense-edit.html')


def delete(request, pk):
    return render(request, 'expense/expense-delete.html')