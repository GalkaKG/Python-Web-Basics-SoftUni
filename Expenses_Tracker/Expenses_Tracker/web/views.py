from django.shortcuts import render, redirect

from Expenses_Tracker.web.forms import ProfileCreateForm
from Expenses_Tracker.web.models import Profile, Expense


def get_profile():
    return Profile.objects.first()


def get_all_expenses():
    return Expense.objects.all()


def home(request):
    profile = get_profile()

    if not profile:
        if request.method == 'GET':
            form = ProfileCreateForm()
        else:
            form = ProfileCreateForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home page')

        context = {
            'profile': profile,
            'form': form
        }

        return render(request, 'profile/home-no-profile.html', context)
    else:
        expenses = get_all_expenses()
        money_left = profile.budget - sum(expenses)

        context = {
            'expenses': expenses,
            'money_left': money_left
        }

        return render(request, 'profile/home-with-profile.html', context)


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