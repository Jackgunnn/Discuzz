from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.models import User


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class PasswordChangeCustomForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user