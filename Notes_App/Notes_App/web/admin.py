from django.contrib import admin
from Notes_App.web.models import ProfileModel, NoteModel


@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    ...


@admin.register(NoteModel)
class NoteAdmin(admin.ModelAdmin):
    ...
