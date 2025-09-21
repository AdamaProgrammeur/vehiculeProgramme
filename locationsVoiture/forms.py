from .models import Voiture, Client
from django import forms

class VoitureForm(forms.ModelForm):
    class Meta:
        model = Voiture
        fields = ['marque', 'modele', 'prix_par_jour', 'disponible', 'image']
       

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'prenom', 'email', 'telephone']
       
