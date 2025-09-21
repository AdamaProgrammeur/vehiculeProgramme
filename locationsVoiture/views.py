from django.shortcuts import render
from .models import Voiture, Client
from .forms import VoitureForm, ClientForm

# Create your views here.

def acceuil(request):
    return render(request, 'acceuil.html')


def listVoiture(request):
    voitures = Voiture.objects.all()  # récupérer toutes les voitures

    return render(request, "voiture.html", {"voitures": voitures})


def ajouter_voiture(request):
    message = ""
    if request.method == 'POST':
        form = VoitureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "valid infos user"
        
    else:
        form = VoitureForm( )
    return render(request, 'ajouter_voiture.html', {'form': form, 'messages': message})


def listClient(request):
    client = Client.objects.all()

    return render(request, "listClient.html", {"client": client})


def ajouter_Client(request):
    message = ""
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            message = "valid infos user"
        
    else:
        form = ClientForm( )

    return render(request, 'ajouterClient.html', {'form': form, 'messages': message})
