from django.urls import path
from .views import acceuil, listVoiture, ajouter_voiture

urlpatterns = [
    path('acceuil/', acceuil, name='acceuil'),
    path('listVoiture/', listVoiture, name='listVoiture'),
    path('ajouter_voiture/', ajouter_voiture, name='ajouter_voiture'),  # ← corrigé
]

# ❌ Ne jamais inclure autogerence.urls ici !
