from django.contrib import admin

from .models import Player, Game


# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user',)


class GameAdmin(admin.ModelAdmin):
    list_display = ('player1', 'player2', 'winner', 'status')


admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)
