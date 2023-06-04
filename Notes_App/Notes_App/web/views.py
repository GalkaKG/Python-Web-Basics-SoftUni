from django.shortcuts import render


def home(request):
    return render(request, 'profile/home-with-profile.html')
