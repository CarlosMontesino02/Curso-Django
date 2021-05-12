from django.shortcuts import render

from .forms import RegForm
# Create your views here.
def inicio(request):
    form = RegForm()
    context = {
        "el_form":form,
    }
    return render(request, "inicio.html", {})