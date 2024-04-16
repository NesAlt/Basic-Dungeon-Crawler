import pygame
from settings import *

class MagicPlayer:
  def __init__(self,animation_player):
    self.animation_player=animation_player
  
  def heal(self,player,amount,cost,groups):
    if player.mana>=cost:
        player.health+=amount
        player.mana-=cost
        if player.health>=player.stats['health']:
          player.health=player.stats['health']
        
        self.animation_player.create_particles('aura',player.rect.center,groups)
        # self.animation_player.create_particles('heal',player.rect.center+pygame.math.Vector2(0,-10),groups)