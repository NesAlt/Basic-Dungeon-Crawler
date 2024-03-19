import pygame
import sys
from settings import *
from ui import Button
from level import level, GAME_OVER


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("RPG")
        self.clock = pygame.time.Clock()
        self.level = level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == GAME_OVER:
                    self.game_over_menu()
                    return

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

    def restart_game(self):
        print("Restarting Game...")
        self.level = level()
        self.run()

    def return_menu(self):
        self.level = None
        main_menu()

    def game_over_menu(self):
        game_over_font = pygame.font.Font(UI_FONT, 40)
        game_over_text = game_over_font.render("Game Over!", True, TEXT_COLOR)
        game_over_text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))

        restart_button = Button(WIDTH // 3, HEIGHT // 2, 200, 50, UI_BG_COLOR, TEXT_COLOR, game_over_font, "Restart",self.restart_game)
        return_button = Button((WIDTH // 3)+20, (HEIGHT // 2)+60, 200, 50, UI_BG_COLOR, TEXT_COLOR, game_over_font,"Return to Main Menu", self.return_menu)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    restart_button.handle_event(event)
                    return_button.handle_event(event)

            self.screen.fill('black')
            self.screen.blit(game_over_text, game_over_text_rect)
            restart_button.draw(self.screen)
            return_button.draw(self.screen)
            pygame.display.update()

def start_game():
    game = Game()
    game.run()


def main_menu():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("RPG")

    font = pygame.font.Font(UI_FONT, 40)
    background_image = pygame.image.load("Assets/background.jpg").convert()
    start_button = Button(WIDTH // 2 - 100, HEIGHT // 2 - 50, 350, 100, UI_BG_COLOR, TEXT_COLOR, font, "Start Game",start_game)
    quit_button = Button(WIDTH // 2 - 100, HEIGHT // 2 + 50, 350, 100, UI_BG_COLOR, TEXT_COLOR, font, "Quit Game",quit_game)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                start_button.handle_event(event)
                quit_button.handle_event(event)

        if background_image:
            screen.blit(background_image, (0, 0))

        start_button.draw(screen)
        quit_button.draw(screen)
        pygame.display.flip()
    pygame.quit()

def quit_game():
    pygame.quit()
    quit()


if __name__ == "__main__":
    main_menu()
