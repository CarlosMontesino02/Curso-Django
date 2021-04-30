from django import forms

class RegFrom(forms.Form):
    nombre = forms.Charfield(max_length=100)
    email = forms.EmailField()
