from django import forms

from Games_Play_App.web.models import ProfileModel, GameModel


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['email', 'age', 'password']

        widgets = {
            'password': forms.PasswordInput
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class DeleteProfileForm(EditProfileForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


class CreateGameForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = '__all__'


class EditGameForm(CreateGameForm):
    ...


class DeleteGameForm(CreateGameForm):
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
