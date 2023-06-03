from django import forms

from Online_Library.web.models import Book, Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class EditProfileForm(ProfileForm):
    ...


class DeleteProfileForm(ProfileForm):
    ...


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
