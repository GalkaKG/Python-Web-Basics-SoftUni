from django.contrib import admin
from Recipes.web.models import Recipe


@admin.register(Recipe)
class Recipe(admin.ModelAdmin):
    pass
