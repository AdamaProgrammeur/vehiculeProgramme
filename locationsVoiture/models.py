from django.db import models

# Create your models here.

class Voiture(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    prix_par_jour = models.DecimalField(max_digits=8, decimal_places=2)
    disponible = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/')

    class Meta:
        managed = True
        verbose_name = 'Voiture'
        verbose_name_plural = 'Voitures'

    def __str__(self):
        return f"{self.marque} {self.modele}"


class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20)

    class Meta:
        managed = True
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return f"{self.nom} {self.prenom}"
