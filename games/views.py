from django.shortcuts import render

from games.models import Player


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def create_game(request):
    players = Player.objects.all()
    context = {'players': players}

    return render(request, 'create_game.html', context)
