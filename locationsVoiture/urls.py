from django.urls import path
from .views import acceuil, listVoiture, ajouter_voiture, listClient, ajouter_Client

urlpatterns = [
    path('acceuil/', acceuil, name='acceuil'),
    path('listVoiture/', listVoiture, name='listVoiture'),
    path('ajouter_voiture/', ajouter_voiture, name='ajouter_voiture'),  # ← corrigé
    path('listClient/', listClient, name='listClient'),
    path('ajouter_Client/', ajouter_Client, name='ajouter_voiture' )
]

# ❌ Ne jamais inclure autogerence.urls ici !
