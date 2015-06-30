from django import forms
import models


class NameForm(forms.Form):
	firstname = forms.CharField(max_length=200)
	lastname = forms.CharField(max_length=200)
	