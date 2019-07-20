from django import forms
from django.core.exceptions import ValidationError

from myapp.models import Member


class SignupForm(forms.ModelForm):
    class Meta:
        model = Member
        widgets = {
            'password': forms.PasswordInput()
        }
        fields = ('username', 'email', 'password',)

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) > 50:
            raise ValidationError('Username must be less than 50')
        return username
