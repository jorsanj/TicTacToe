from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Game(models.Model):
    STATUS = (
        (0, 'Pendiente'),
        (1, 'Finalizada'),
    )

    board = models.CharField(max_length=9, default='---------')
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='games_p1')
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='games_p2')
    winner = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"Partida {self.id}: {self.player1.user.username} - {self.player2.user.username}"
