from django import forms
from My_Music_App.web.models import Profile, Album


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class EditAlbumForm(CreateAlbumForm):
    pass


class DeleteAlbumForm(CreateAlbumForm):
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


