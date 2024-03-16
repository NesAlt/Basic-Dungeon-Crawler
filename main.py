import pygame
from settings import *

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

  def draw(self):
    pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    screen.blit(self.text_surface, self.text_rect)

  def handle_event(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_x, mouse_y = event.pos
      if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
        self.action()

        
def start_game():
  import pygame,sys
  from settings import WIDTH,HEIGHT,FPS
  from level import level
  class Game:
    def __init__(self):
      pygame.init()
      self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
      pygame.display.set_caption("RPG")
      self.clock=pygame.time.Clock()

      self.level =level()



    def run(self):
      while True:
        for event in pygame.event.get():
          if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        self.screen.fill('black')
        self.level.run()
        pygame.display.update()
        self.clock.tick(FPS)

  if __name__ == "__main__":
      game=Game()
      game.run()

def quit_game():
  pygame.quit()
  quit()

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RPG")


font = pygame.font.Font(UI_FONT, 40)
text_color = (TEXT_COLOR)
button_color = (UI_BG_COLOR) 
button_text_color = (TEXT_COLOR)


background_image = pygame.image.load("Assets/background.jpg").convert()


start_button = Button(WIDTH // 2 - 100, HEIGHT // 2 - 50, 350, 100, button_color, button_text_color, font, "Start Game", start_game)
quit_button = Button(WIDTH // 2 - 100, HEIGHT  // 2 + 50, 350, 100, button_color, button_text_color, font, "Quit Game", quit_game)

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.MOUSEBUTTONDOWN:
      start_button.handle_event(event)
      quit_button.handle_event(event)

  if background_image:
    screen.blit(background_image, (0, 0))

  start_button.draw()
  quit_button.draw()
  pygame.display.flip()
pygame.quit()
