from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Llibre, Propietari, Lector
from .forms import LlibreForm, PropietariForm, LectorForm
from django.views.generic import TemplateView, View, FormView, DetailView, ListView


def multi_form_view(request):
    if request.method == 'POST':
        llibre_form = LlibreForm(request.POST, request.FILES)
        propietari_form = PropietariForm(request.POST)
        lector_form = LectorForm(request.POST)
        if llibre_form.is_valid() and propietari_form.is_valid() and lector_form.is_valid():
            llibre= llibre_form.save()
            propietari = propietari_form.save(commit=False) 
            propietari.save() 
            lector = lector_form.save(commit=False) 
            lector.llib_nom_fk = llibre # Asignar el libro al lector 
            lector.save()
            # Puedes redirigir a otra página después de guardar los formularios
            return redirect('perfil')
    else:
        llibre_form = LlibreForm()
        propietari_form = PropietariForm()
        lector_form = LectorForm()
    
    context = {
        'llibre_form': llibre_form,
        'propietari_form': propietari_form,
        'lector_form': lector_form,
    }
    return render(request, 'lectures2025/formulario.html', context)


class HomeView(TemplateView):
    template_name = "lectures2025/home.html"
    context_object_name = ""


class afegir_llibre(FormView):
    template_name = "lectures2025/formulario.html"
    
    def get(self, request): 
        form = LlibreForm() 
        return render(request, self.template_name, {'form': form}) 
    
    def post(self, request, *args, **kwargs): 
        form = LlibreForm(request.POST, request.FILES)  
        if form.is_valid(): 
            form.save() 
            return redirect('home')  # Redirigir después de guardar 
        return self.render_to_response({'form': form})
    
class LectorListView(ListView): 
    model = Lector 
    template_name = "lectures2025/llista_lectors.html" 
    context_object_name = "llista_lectors"

    def get_queryset(self):
        return Lector.objects.all()

class Perfil_lector(DetailView): 
    model = Lector 
    template_name = "lectures2025/perfil_lector.html" 
    context_object_name = "perfil_lector" 
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context['llibres'] = Llibre.objects.filter(llib_lector=self.object) 
        return context
    