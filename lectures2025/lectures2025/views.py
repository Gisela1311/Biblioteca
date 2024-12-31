from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Llibre, Propietari, Lector
from .forms import LlibreForm, PropietariForm, LectorForm

def home(request):
    return render(request, 'base.html')

def add_llibre(request):
    if request.method == 'POST':
        form = LlibreForm(request.POST, request.FILES)  # Asegúrate de incluir request.FILES
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = LlibreForm()
    return render(request, 'formulario.html', {'form': form})

def perfil(request, prop_id):
    propietari = get_object_or_404(Propietari, pk=prop_id)
    llibres = Llibre.objects.filter(llib_propietari=propietari)
    return render(request, 'perfil.html', {'propietari': propietari, 'llibres': llibres})
