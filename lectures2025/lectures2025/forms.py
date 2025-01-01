from django import forms
from .models import Llibre, Propietari, Lector

class LlibreForm(forms.ModelForm):
    class Meta:
        model = Llibre
        fields = ['llib_nom', 'llib_autor', 'llib_editorial', 'llib_genere', 'llib_pagines', 'llib_data_lectura', 'llib_portada']

class PropietariForm(forms.ModelForm):
    class Meta:
        model = Propietari
        fields = ['prop_nom']

class LectorForm(forms.ModelForm):
    class Meta:
        model = Lector
        fields = ['lec_nom']
