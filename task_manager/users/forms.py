from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, SetPasswordForm
from django import forms
from django.utils.translation import gettext
User = get_user_model()


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'username']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=gettext("old_password"),
    )
    new_password2 = forms.CharField(label=gettext("new_password"))
