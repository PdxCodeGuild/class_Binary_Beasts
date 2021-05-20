from django import forms
class Url(forms.Form):
    shortURL = forms.CharField(label="URL")