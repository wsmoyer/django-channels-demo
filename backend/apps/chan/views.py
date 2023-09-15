from django.http import HttpResponse
from django.shortcuts import render

from .forms import FavoriteAnimalForm
from .models import FavoriteAnimal
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.transform import factor_cmap


def save_fav_animal(message):
    form = FavoriteAnimalForm({
                'animal_choice': message
            })       
    form.save()


def show_chart(color):
    dog_count = FavoriteAnimal.objects.filter(animal_choice='Dog').count()
    cat_count = FavoriteAnimal.objects.filter(animal_choice='Cat').count()
    horse_count = FavoriteAnimal.objects.filter(animal_choice='Horse').count()

    animals = ['Dog', 'Cat', 'Horse']
    counts = [dog_count, cat_count, horse_count]


    p = figure(x_range=animals, title="Favorite Animal Votes", x_axis_label="Animal", y_axis_label="Count")

    source = ColumnDataSource(data=dict(animals=animals, counts=counts))

    p.vbar(x='animals', top='counts',source=source, legend_field="animals", width=0.5, bottom=0, color=color,
    line_color='white', fill_color=factor_cmap('animals', palette=Spectral6, factors=animals)
    )

    p.y_range.start = 0
    p.y_range.end = 9
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"

    script, div = components(p)

    return {
        'script':script,
        'div': div
    }


def index(request):
    vals = show_chart('green')

    return render(request, 'index.html', {
        'form': FavoriteAnimalForm,
         'script': vals['script'],
         'div': vals['div']

    })
