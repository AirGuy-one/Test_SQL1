from django import forms
from .models import TestData


class TestDataForm(forms.ModelForm):
    class Meta:
        model = TestData
        fields = ['title', 'text', 'cat', 'population']
