from django.db import models

# Create your models here.

class FavoriteAnimal(models.Model):
    animalChoices = models.TextChoices('AnimalChoice','Cat Dog Horse')
    animal_choice = models.CharField(max_length=100, choices=animalChoices.choices)