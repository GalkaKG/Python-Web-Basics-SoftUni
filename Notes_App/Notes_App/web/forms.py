from django import forms
from Notes_App.web.models import ProfileModel, NoteModel


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = NoteModel
        fields = ['title', 'content', 'image_url']


class EditNoteForm(CreateNoteForm):
    ...


class DeleteNoteForm(CreateNoteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.disabled = True
