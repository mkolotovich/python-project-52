from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'password1', 'password2']


class CustomUserChangeForm(UserCreationForm):
    def clean_username(self):
        username = self.cleaned_data.get("username")
        return username
