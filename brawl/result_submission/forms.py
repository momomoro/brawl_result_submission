from django import forms

players = [("Divock", "Divock"), ("Games", "Games"), ("griffs", "griffs")]


class PlayerForm(forms.Form):
    player1 = forms.ChoiceField(label='Player 1', choices=players,
                                widget=forms.Select(attrs={'data-player': 'player1'}))
    player2 = forms.ChoiceField(label='Player 2', choices=players,
                                widget=forms.Select(attrs={'data-player': 'player2'}))


class GameResultForm(forms.Form):
    player1_deck = forms.ChoiceField(label='Player 1 Deck')
    player2_deck = forms.ChoiceField(label='Player 2 Deck')

    win = forms.ChoiceField(choices=[('player1', 'player1'), ('player2', 'player2')], widget=forms.RadioSelect, label='Who Won?')
    play = forms.ChoiceField(choices=[('player1', 'player1'), ('player2', 'player2')], widget=forms.RadioSelect, label='Who Was On The Play')
