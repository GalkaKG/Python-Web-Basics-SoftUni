from django import forms

from My_Plant_App.web.models import ProfileModel


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ('profile_picture',)




