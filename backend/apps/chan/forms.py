from pyexpat import model
from django import forms
from .models import FavoriteAnimal

class FavoriteAnimalForm(forms.ModelForm):
    class Meta:
        model = FavoriteAnimal
        fields = '__all__'