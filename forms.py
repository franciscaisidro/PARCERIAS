from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioFrom(UserCreationForm):
    contato = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'contato', 'password1', 'password2']