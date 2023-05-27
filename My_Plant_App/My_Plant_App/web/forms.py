from django import forms

from My_Plant_App.web.models import ProfileModel, PlantModel


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ('profile_picture',)


class ProfileEditForm(ProfileCreateForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class ProfileDeleteForm(ProfileCreateForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance


class CreatePlantForm(forms.ModelForm):
    class Meta:
        model = PlantModel
        fields = '__all__'


class EditPlantForm(CreatePlantForm):
    ...


class DeletePlantForm(CreatePlantForm):
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
