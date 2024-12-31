from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Llibre, Propietari, Lector
from .forms import LlibreForm, PropietariForm, LectorForm
from django.views.generic import TemplateView, View, FormView 

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
    

class perfil_lector(View):
    template_name="lectures2025/perfil.html"

    def get(self, request, pk): 
        lector = get_object_or_404(Lector, pk=pk)
        llibres = Llibre.objects.filter(llib_lector=lector) 
        return render(request, self.template_name, {'lector': lector, 'llibres': llibres})
