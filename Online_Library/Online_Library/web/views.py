from django.shortcuts import render, redirect

from Online_Library.web.forms import AddBookForm, ProfileForm, EditProfileForm
from Online_Library.web.models import Profile, Book


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def get_all_books():
    return Book.objects.all()


def get_book(pk):
    return Book.objects.filter(pk=pk).get()


def index(request):
    profile = get_profile()

    if profile:
        return home_with_user(request)

    return home_without_user(request)


def home_with_user(request):
    profile = get_profile()
    books = get_all_books()

    context = {
        'profile': profile,
        'books': books
    }

    return render(request, 'home/home-with-profile.html', context)


def home_without_user(request):

    if request.method == 'GET':
        form = ProfileForm()
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home page')

    context = {
        'form': form
    }

    return render(request, 'home/home-no-profile.html', context)


def add_book(request):
    if request.method == 'GET':
        form = AddBookForm()
    else:
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home page')

    context = {
        'form': form
    }

    return render(request, 'book/add-book.html', context)


def edit_book(request, pk):
    return render(request, 'book/edit-book.html')


def book_details(request, pk):
    return render(request, 'book/book-details.html')


def profile(request):
    profile = get_profile()
    context = {
        'profile': profile
    }
    return render(request, 'profile/profile.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
        return redirect('profile')

    context = {
        'form': form
    }

    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    return render(request, 'profile/delete-profile.html')
