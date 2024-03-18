import pygame
class weapon(pygame.sprite.Sprite):
  def __init__(self,player,groups):
    super().__init__(groups)
    self.sprite_type='weapon'
    direction=player.status.split('_')[0]

    full_path=f'Assets//weapons//{player.weapon}//{direction}.png'
    self.image=pygame.image.load(full_path).convert_alpha()

    if direction=='right':
      self.rect=self.image.get_rect(midleft=player.rect.midright+pygame.math.Vector2(-20,5))
    elif direction=='left':
      self.rect=self.image.get_rect(midright=player.rect.midleft+pygame.math.Vector2(25,5))
    elif direction=='down':
      self.rect=self.image.get_rect(midtop=player.rect.midbottom+pygame.math.Vector2(5,-3))
    else:
      self.rect=self.image.get_rect(midbottom=player.rect.midtop+pygame.math.Vector2(5,15))
