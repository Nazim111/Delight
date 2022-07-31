from django import forms
from .models import *
from django.forms import TextInput


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["name", "number"]

        widgets = {
            'name': TextInput(attrs={
                'class': 'name',
                'placeholder': 'Ваше имя'
            }),
            'number': TextInput(attrs={
                'class': 'number',
                'placeholder': 'Номер телефона'
            })
        }