from django.contrib import admin

from Games_Play_App.web.models import ProfileModel, GameModel


@admin.register(ProfileModel)
class Profile(admin.ModelAdmin):
    ...


@admin.register(GameModel)
class Game(admin.ModelAdmin):
    ...



