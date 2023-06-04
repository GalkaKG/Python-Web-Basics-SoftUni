from django import forms
from Notes_App.web.models import ProfileModel, NoteModel


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = NoteModel
        fields = '__all__'
