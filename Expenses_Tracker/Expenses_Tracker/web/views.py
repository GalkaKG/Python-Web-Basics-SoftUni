from django.shortcuts import render, redirect

from Expenses_Tracker.web.forms import ProfileCreateForm, ExpenseCreateForm, ExpenseEditForm, ExpenseDeleteForm, \
    ProfileEditForm
from Expenses_Tracker.web.models import Profile, Expense


def get_profile():
    return Profile.objects.first()


def get_all_expenses():
    return Expense.objects.all()


def get_expense(pk):
    return Expense.objects.get(pk=pk)


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
        money_left = profile.budget - sum([expense.price for expense in expenses])

        context = {
            'profile': profile,
            'expenses': expenses,
            'money_left': money_left
        }

        return render(request, 'profile/home-with-profile.html', context)


def profile_page(request):
    profile = get_profile()
    expenses = get_all_expenses()
    money_left = profile.budget - sum([expense.price for expense in expenses])

    context = {
        'profile': profile,
        'count_expenses': len(expenses),
        'money_left': money_left
    }

    return render(request, 'profile/profile.html', context)


def profile_edit(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form
    }

    return render(request, 'profile/profile-edit.html', context)


def profile_delete(request):
    profile = get_profile()
    expenses = get_all_expenses()

    if request.method == 'POST':
        expenses.delete()
        profile.delete()
        return redirect('home page')

    return render(request, 'profile/profile-delete.html')


def create(request):
    if request.method == 'GET':
        form = ExpenseCreateForm()
    else:
        form = ExpenseCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form
    }

    return render(request, 'expense/expense-create.html', context)


def edit(request, pk):
    expense = get_expense(pk)

    if request.method == 'GET':
        form = ExpenseEditForm(instance=expense)
    else:
        form = ExpenseEditForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form
    }

    return render(request, 'expense/expense-edit.html', context)


def delete(request, pk):
    expense = get_expense(pk)

    if request.method == 'GET':
        form = ExpenseDeleteForm(instance=expense)
    else:
        form = ExpenseDeleteForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form
    }
    return render(request, 'expense/expense-delete.html', context)
