from django.contrib import admin
from .models import Voiture

# Register your models here.

class voitureAdmin(admin.ModelAdmin):
    list_display = ("id", "marque", "modele", "prix_par_jour", "disponible")  # colonnes affichées
    list_filter = ("disponible", "marque")  # filtres à droite
    search_fields = ("marque", "modele")  # barre de recherche



admin.site.register(Voiture, voitureAdmin)