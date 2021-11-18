from django import forms
from .common import get_players, get_sheet, SHEET_ID, RANGE

players = [("Divock", "Divock"), ("Games", "Games"), ("griffs", "griffs")]


class PlayerForm(forms.Form):
    player1 = forms.ChoiceField(label='Player 1',
                                widget=forms.Select(attrs={'data-player': 'player1'}))
    player2 = forms.ChoiceField(label='Player 2',
                                widget=forms.Select(attrs={'data-player': 'player2'}))

    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        sheet = get_sheet(SHEET_ID, RANGE)
        players = get_players(sheet['values'])
        self.fields['player1'].choices = [(player, player) for player in players]
        self.fields['player2'].choices = [(player, player) for player in players]


class GameResultForm(forms.Form):
    player1_deck = forms.ChoiceField(label='Player 1 Deck')
    player2_deck = forms.ChoiceField(label='Player 2 Deck')

    win = forms.ChoiceField(choices=[('player1', 'player1'), ('player2', 'player2')], widget=forms.RadioSelect, label='Who Won?')
    play = forms.ChoiceField(choices=[('player1', 'player1'), ('player2', 'player2')], widget=forms.RadioSelect, label='Who Was On The Play')
