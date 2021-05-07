from django import forms
from .models import Registrado

class RegModelForm(forms.ModeLForm):
    class Meta:
        model = Registrado
        fields = ["nombre","email]
        def clean_email(self):
            print self.cleaned_data.get("email")
            email_base, proveedor = email.split("@")
            dominio, extension = proveedor.split(".")
            if not extension in email:
                raise forms.ValidationError("Email no valido")
            return email
class RegFrom(forms.Form):
    nombre = forms.Charfield(max_length=100)
    email = forms.EmailField()
