from django import forms

from Online_Library.web.models import Book, Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class EditProfileForm(ProfileForm):
    ...


class DeleteProfileForm(ProfileForm):
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


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class EditBookForm(AddBookForm):
    ...
