from django import forms
from .models import Link


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('long_url',)

        widget = forms.URLInput(
            attrs={'placeholder': 'https://anc.ua/ru/item/renni-z-apelsinovim-smakom-tabletki-zhuvalni-24-27890',
                   'required': 'true'},
        )

