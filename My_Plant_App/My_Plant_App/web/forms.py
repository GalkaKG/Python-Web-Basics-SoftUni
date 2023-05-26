from django import forms

from My_Plant_App.web.models import ProfileModel, PlantModel


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ('profile_picture',)


class CreatePlantForm(forms.ModelForm):
    class Meta:
        model = PlantModel
        fields = '__all__'



