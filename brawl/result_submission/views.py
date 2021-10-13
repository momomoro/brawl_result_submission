from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.forms import formset_factory

# Create your views here.

from .forms import PlayerForm, GameResultForm

# TODO: load this from google
all_decks = {"Divock": ["Domri", "Koma", "Yawg", "Valki"],
         "Games": ["Sythis", "Tamiyo", "Feather", "Zareth"],
         "griffs": ["Yawg", "Chandra", "Teferi", "Esika"]}


def index(request):
    if request.method == 'POST':
        # TODO: check form for correctness
        # TODO: submit results to google
        return HttpResponse("Thanks for your submission")
    else:
        players = PlayerForm()
        game_formset = formset_factory(GameResultForm, extra=5)
    context = {'players': players, 'games': game_formset}
    return render(request, 'result_submission.html', context)


def load_decks(request):
    player = request.GET.get('player')
    decks = all_decks[player]
    return render(request, 'deck_dropdown.html', {'decks': decks})
