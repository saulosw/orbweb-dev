from typing import Any
from django import forms
from django.core.exceptions import ValidationError
import re
from orbweb.models import UserProfile

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
        model = UserProfile
        fields = [
            'username',
            'profile_pic',
            'bio',
            'password',
        ]

        labels = {
            'username': 'Nickname',
            'profile_pic': 'Foto de Perfil',
            'bio': 'Bio',
            'password': 'Senha',
        }

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Digite seu nickname aqui'
            }),
            'profile_pic': forms.ClearableFileInput(),
            'bio': forms.Textarea(attrs={
                'placeholder': 'Escreva uma breve bio'
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
            raise ValidationError({
                'confirm_password': [
                    ValidationError('As senhas não correspondem.', code='invalid')
                ]
            })
        return cleaned_data