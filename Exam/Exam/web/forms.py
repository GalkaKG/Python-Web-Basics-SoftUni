from django import forms
from Exam.web.models import ProfileModel, FruitModel


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Password'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name', 'image_url', 'age']


class CreateFruitForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Name'
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Fruit Image URL'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Description'
                }
            ),
            'nutrition': forms.TextInput(
                attrs={
                    'placeholder': 'Nutrition Info'
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""


class EditFruitForm(CreateFruitForm):
    ...


class DeleteFruitForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = ['name', 'image_url', 'description']

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
