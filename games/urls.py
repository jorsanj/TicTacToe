from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_game/', views.create_game, name='create_game'),
    path('play_game/<int:game_id>/', views.play_game, name='play_game'),
]
