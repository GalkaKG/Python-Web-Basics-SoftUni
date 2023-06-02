from django.shortcuts import render


def index(request):
    return render(request, 'home/home-with-profile.html')


def add_book(request):
    return render(request, 'book/add-book.html')


def edit_book(request, pk):
    return render(request, 'book/edit-book.html')


def book_details(request, pk):
    return render(request, 'book/book-details.html')


def profile(request):
    return render(request, 'profile/profile.html')


def edit_profile(request):
    return render(request, 'profile/edit-profile.html')


def delete_profile(request):
    return render(request, 'profile/delete-profile.html')
