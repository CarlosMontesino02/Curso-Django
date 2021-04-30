from django.shortcuts import render
from .forms import RegForm
from .models import Registrado

def inicio(request):
    form = RegForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        abc = form_data.get("email")
        obj = Regsitado.objects.create(email=abc)
        abc2 = Registrado.objects.create(email=abc, nombre=abc2)

    context = {
        "el_form": form,
    }
    return render (request, "inicio.html", context)
