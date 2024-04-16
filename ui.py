import pygame
from settings import *

class UI:
    def __init__(self):
        
        self.display_surface=pygame.display.get_surface()
        self.font=pygame.font.Font(UI_FONT,UI_FONT_SIZE)

        self.health_bar_rect=pygame.Rect(10,10,HEALTH_BAR_WIDTH,BAR_HEIGHT)
        self.mana_bar_rect=pygame.Rect(10,34,MANA_BAR_WIDTH,BAR_HEIGHT)

        self.weapon_graphics=[]
        for weapon in weapon_data.values():
            path = weapon['graphic']
            weapon = pygame.image.load(path).convert_alpha()
            self.weapon_graphics.append(weapon)


    def show_bar(self,current_amount,max_amount,bg_rect,color):
        
        pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)

        ratio=current_amount/max_amount
        current_width=bg_rect.width*ratio
        current_rect=bg_rect.copy()
        current_rect.width=current_width

        pygame.draw.rect(self.display_surface,color,current_rect)
        pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rect,3)
    
    # def show_armor(self,armor_rating):
    #     text_surf=self.font.render(str(int(armor_rating)),False,TEXT_COLOR)

    #     text_rect=text_surf.get_rect(topleft=(160,34))
    #     pygame.draw.rect(self.display_surface,UI_BG_COLOR,text_rect.inflate(6,6))
    #     self.display_surface.blit(text_surf,text_rect)
    #     pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,text_rect.inflate(6,6),3)

    def selection_box(self,left,top):
        bg_rect=pygame.Rect(left,top,ITEM_BOX_SIZE,ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)
        pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rect,3)
        return bg_rect

    def weapon_overlay(self,weapon_index):

      bg_rect=self.selection_box(10,680)
      weapon_surf = self.weapon_graphics[weapon_index]
      weapon_rect = weapon_surf.get_rect(center = bg_rect.center)
      
      self.display_surface.blit(weapon_surf,weapon_rect)

        
    def display(self,player):
        self.show_bar(player.health,player.stats['health'],self.health_bar_rect,HEALTH_COLOR)
        self.show_bar(player.mana,player.stats['mana'],self.mana_bar_rect,MANA_COLOR)

        # self.show_armor(player.armor)
        
        self.weapon_overlay(player.weapon_index)

class Button:
  def __init__(self, x, y, width, height, color, text_color, font, text, action):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.color = color
    self.text_color = text_color
    self.font = font
    self.text = text
    self.action = action
    self.text_surface = self.font.render(self.text, True, self.text_color)
    self.text_rect = self.text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))

  def draw(self, screen):
    pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    screen.blit(self.text_surface, self.text_rect)

  def handle_event(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_x, mouse_y = event.pos
      if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
        self.action()