from django import forms
from Car_Collection_App.web.models import Profile, Car


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']
        widgets = {
            'password': forms.TextInput(
                attrs={'type': 'password'}
            )
        }


class CreateProfileForm(BaseProfileForm):
    ...


class EditProfileForm(BaseProfileForm):
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
