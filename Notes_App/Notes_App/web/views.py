from django.shortcuts import render, redirect

from Notes_App.web.forms import CreateProfileForm
from Notes_App.web.models import ProfileModel, NoteModel


def get_profile():
    try:
        return ProfileModel.objects.get()
    except ProfileModel.DoesNotExist:
        return None


def get_all_notes():
    return NoteModel.objects.all()


def get_note(pk):
    return NoteModel.objects.filter(pk=pk).get()


def home(request):
    profile = get_profile()

    if profile:
        return home_with_profile(request)

    return home_without_profile(request)


def home_with_profile(request):
    profile = get_profile()
    notes = get_all_notes()

    context = {
        'profile': profile,
        'notes': notes
    }

    return render(request, 'profile/home-with-profile.html', context)


def home_without_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('profile')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'profile/home-no-profile.html', context)


def profile_page(request):
    profile = get_profile()
    notes = get_all_notes()

    context = {
        'profile': profile,
        'count_notes': len(notes)
    }

    return render(request, 'profile/profile.html', context)


def add_note(request):
    return render(request, 'note/note-create.html')


def edit_note(request, pk):
    return render(request, 'note/note-edit.html')


def delete_note(request, pk):
    return render(request, 'note/note-delete.html')


def details_note(request, pk):
    return render(request, 'note/note-details.html')
