from django.shortcuts import render, redirect

from Recipes.web.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from Recipes.web.models import Recipe


def home_page(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes
    }

    return render(request, 'index.html', context)


def create(request):
    if request.method == 'GET':
        form = CreateRecipeForm()
    else:
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form
    }

    return render(request, 'create.html', context)


def edit(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'GET':
        form = EditRecipeForm(instance=recipe)
    else:
        form = EditRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form
    }

    return render(request, 'edit.html', context)


def delete(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'GET':
        form = DeleteRecipeForm(instance=recipe)
    else:
        form = DeleteRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'recipe': recipe,
        'form': form
    }

    return render(request, 'delete.html', context)


def details(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    context = {
        'recipe': recipe
    }

    return render(request, 'details.html', context)
