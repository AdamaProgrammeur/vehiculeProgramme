from django.contrib import admin
from .models import Voiture, Client

# Register your models here.

class voitureAdmin(admin.ModelAdmin):
    list_display = ("id", "marque", "modele", "prix_par_jour", "disponible")  # colonnes affichées
    list_filter = ("disponible", "marque")  # filtres à droite
    search_fields = ("marque", "modele")  # barre de recherche



class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'telephone')
    search_fields = ('nom', 'prenom', 'email')


admin.site.register(Voiture, voitureAdmin)
admin.site.register(Client, ClientAdmin)