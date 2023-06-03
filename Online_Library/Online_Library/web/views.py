from django.shortcuts import render, redirect

from Online_Library.web.forms import AddBookForm, ProfileForm, EditProfileForm, DeleteProfileForm, EditBookForm
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
    book = get_book(pk)

    if request.method == 'GET':
        form = EditBookForm(instance=book)
    else:
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('home page')

    context = {
        'book': book,
        'form': form
    }
    return render(request, 'book/edit-book.html', context)


def delete_book(request, pk):
    book = get_book(pk)
    book.delete()
    
    return redirect('home page')


def book_details(request, pk):
    book = get_book(pk)

    context = {
        'book': book
    }

    return render(request, 'book/book-details.html', context)


def profile_page(request):
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
    profile = get_profile()
    books = get_all_books()

    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        form.save()
        books.delete()
        return redirect('home page')

    context = {
        'form': form
    }

    return render(request, 'profile/delete-profile.html', context)
