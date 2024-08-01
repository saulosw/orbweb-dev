from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError('Senha fraca.')



class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
                'placeholder': 'Digite sua senha aqui'
        }),
        validators=[strong_password]
    )
    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite a senha novamente'
        }),
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'username': 'Nickname',
            'email': 'Email',
            'password': 'Senha',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Digite seu primeiro nome aqui'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Digite seu sobrenome aqui'
            }),
            'username': forms.TextInput(attrs={
                'placeholder': 'Digite seu nickname aqui'
            })
            ,
            'email': forms.TextInput(attrs={
                'placeholder': 'Digite seu email aqui'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Digite sua senha aqui'
            }),
        }

    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            password_confirm_error = ValidationError(
                'As senha não corresponde.',
                code='invalid'
            )
            raise ValidationError({
                'confirm_password': [
                    password_confirm_error,
                ],
            })