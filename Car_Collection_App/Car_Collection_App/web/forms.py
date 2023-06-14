from django import forms
from Car_Collection_App.web.models import Profile, Car


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']


class CreateProfileForm(BaseProfileForm):
    ...


class EditProfileForm(BaseProfileForm):
    ...


class DeleteProfileForm(BaseProfileForm):
    ...


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CreateCarForm(BaseCarForm):
    ...


class EditCarForm(BaseCarForm):
    ...


class DeleteCarForm(BaseCarForm):
    ...
