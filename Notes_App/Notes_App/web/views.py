from django.shortcuts import render


def home(request):
    return render(request, 'profile/home-with-profile.html')


def home_without_profile(request):
    return render(request, 'profile/home-no-profile.html')


def profile(request):
    return render(request, 'profile/profile.html')


def add_note(request):
    return render(request, 'note/note-create.html')


def edit_note(request, pk):
    return render(request, 'note/note-edit.html')


def delete_note(request, pk):
    return render(request, 'note/note-delete.html')


def details_note(request, pk):
    return render(request, 'note/note-details.html')
