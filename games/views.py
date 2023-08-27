from django.http import HttpResponse
from django.shortcuts import render, redirect

from games.models import Player, Game


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def create_game(request):
    if request.method == 'POST':
        player1_id = request.POST.get('player1')
        player1 = Player.objects.get(pk=player1_id)

        player2_id = request.POST.get('player2')
        player2 = Player.objects.get(pk=player2_id)

        game = Game.objects.create(player1=player1, player2=player2)

        return redirect('play_game', game_id=game.id)

    players = Player.objects.all()
    context = {'players': players}

    return render(request, 'create_game.html', context)


def play_game(request, game_id):
    game = Game.objects.get(id=game_id)

    if game.status == 1:
        return HttpResponse('Esta partida ya finalizó.')

    current_player = 'player1' if game.board.count('X') == game.board.count('X') else player2
    context = {'game': game, 'current_player': current_player}

    return render(request, 'play_game.html', context)
