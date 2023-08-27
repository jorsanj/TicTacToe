from django.http import HttpResponse, JsonResponse
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

    current_player = 'player1' if game.board.count('X') == game.board.count('X') else 'player2'
    context = {'game': game, 'current_player': current_player}

    return render(request, 'play_game.html', context)


def apply_election(board, symbol, cell):
    board_list = list(board)
    board_list[cell - 1] = symbol
    new_board = ''.join(board_list)

    return new_board


def check_and_update_game(request):
    data = {}
    if request.method == 'POST':
        game_id = request.POST.get('game_id')
        game = Game.objects.get(id=game_id)

        cell = int(request.POST.get('cell_election'))
        symbol = 'X' if game.board.count('X') == game.board.count('O') else 'O'
        data['symbol'] = symbol

        board = apply_election(game.board, symbol, cell)
        data['board'] = board

        if check_win(board, symbol):
            game.status = 1
            game.winner = game.player1 if symbol == 'X' else game.player2
            game.save()
            data['is_win'] = True
            data['winner'] = game.winner.user.username

        elif '-' not in board:
            game.status = 1
            game.save()
            data['is_draw'] = True

        game.board = board
        game.save()

        data['success'] = True

    return JsonResponse(data)


def check_win(board, symbol):
    lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for line in lines:
        if all(board[i] == symbol for i in line):
            return True
    return False
