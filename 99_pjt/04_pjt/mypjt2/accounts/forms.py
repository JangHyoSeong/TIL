from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms

user = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = user
        fields = ('username', 'email', 'first_name', 'last_name', )


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = user
        fields = ('email', 'first_name', 'last_name', 'username',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password')