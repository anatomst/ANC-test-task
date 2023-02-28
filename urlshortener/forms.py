from django import forms
from .models import Link


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('long_url',)

        widgets = {
            'long_url': forms.TextInput(attrs={'class': 'form-control'}),
        }
