from django.shortcuts import render, redirect

from Notes_App.web.forms import CreateProfileForm, CreateNoteForm, EditNoteForm, DeleteNoteForm
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


def profile_delete(request):
    profile = get_profile()
    notes = get_all_notes()

    profile.delete()
    for note in notes:
        note.delete()

    return redirect('home page')


def add_note(request):
    if request.method == 'GET':
        form = CreateNoteForm()
    else:
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home page')

    context = {
        'form': form
    }

    return render(request, 'note/note-create.html', context)


def edit_note(request, pk):
    note = get_note(pk)

    if request.method == 'GET':
        form = EditNoteForm(instance=note)
    else:
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
        return redirect('home page')

    context = {
        'note': note,
        'form': form
    }

    return render(request, 'note/note-edit.html', context)


def delete_note(request, pk):
    note = get_note(pk)

    if request.method == 'GET':
        form = DeleteNoteForm(instance=note)
    else:
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
        return redirect('home page')

    context = {
        'note': note,
        'form': form
    }

    return render(request, 'note/note-delete.html', context)


def details_note(request, pk):
    note = get_note(pk)

    context = {
        'note': note
    }

    return render(request, 'note/note-details.html', context)
