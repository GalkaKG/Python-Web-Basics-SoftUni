from django.contrib import admin

from My_Plant_App.web.models import ProfileModel, PlantModel


@admin.register(ProfileModel)
class Profile(admin.ModelAdmin):
    ...


@admin.register(PlantModel)
class Plant(admin.ModelAdmin):
    ...
