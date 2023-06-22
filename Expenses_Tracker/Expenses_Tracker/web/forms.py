from django import forms
from Expenses_Tracker.web.models import Profile, Expense


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['budget', 'first_name', 'last_name', 'profile_image']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_image': 'Profile Image'
        }


class ProfileEditForm(ProfileCreateForm):
    ...


class ExpenseCreateForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'description', 'expense_image', 'price']
        labels = {
            'expense_image': 'Expense Image'
        }


class ExpenseEditForm(ExpenseCreateForm):
    ...


class ExpenseDeleteForm(ExpenseCreateForm):
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
