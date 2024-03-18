import pygame
from settings import *
from ui import Button

        
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

  start_button.draw(screen)
  quit_button.draw(screen)
  pygame.display.flip()
pygame.quit()
