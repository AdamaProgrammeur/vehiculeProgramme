from .models import Voiture
from django import forms

class VoitureForm(forms.ModelForm):
    class Meta:
        model = Voiture
        fields = ['marque', 'modele', 'prix_par_jour', 'disponible', 'image']
       
