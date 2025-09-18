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
