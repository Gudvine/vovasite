from django import forms

from .models import Videomaker


class SearchForm(forms.Form):
	query = forms.ChoiceField()
