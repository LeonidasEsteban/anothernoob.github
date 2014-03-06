from django.forms import ModelForm
from django import forms

class SummonerForm(forms.Form):
    nickname = forms.CharField(label = '', required = True)