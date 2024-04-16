import pygame
import sys
from settings import *
from ui import Button
from level import Level, GAME_OVER,YSortCameraGroup

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("RPG")
        self.clock = pygame.time.Clock()

        self.level_selection_menu()
    
    def level_selection_menu(self):
        level_buttons = []
        for idx, level_name in enumerate(LEVELS):
            level_button = Button(WIDTH // 2 - 100, HEIGHT // 2 - 100 + idx * 75, 200, 50, UI_BG_COLOR, TEXT_COLOR, BUTTON_FONT,level_name,
                                  lambda name=level_name: self.start_level(name))
            level_buttons.append(level_button)

        background_image = pygame.image.load("Assets/level back2.jpg").convert()


        running = True
        while running:
            handle_events(*level_buttons)
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         running = False
            #         pygame.quit()
            #         sys.exit()
            if background_image:
                self.screen.blit(background_image, (0, 0))
            for button in level_buttons:
                button.draw(self.screen)

            pygame.display.update()

    def start_level(self,level_name):
        self.level = Level(level_name,f'Assets\Map\{level_name}\{level_name}.png')
        self.floor_surface = pygame.image.load(f'Assets\Map\{level_name}\{level_name}.png').convert()
        self.camera_group = YSortCameraGroup(self.floor_surface)
        self.run()

    def victory_menu(self):
        victory_font = pygame.font.Font(UI_FONT, 40)
        victory_text = victory_font.render("Victory!", True, TEXT_COLOR)
        victory_text_rect = victory_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        background_image = pygame.image.load("Assets/victory back.jpg").convert()

        return_button = Button((WIDTH // 3)-150, HEIGHT // 2, 650, 50, UI_BG_COLOR, TEXT_COLOR, victory_font, "Return to Main Menu", self.return_menu)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    return_button.handle_event(event)

            if background_image:
                self.screen.blit(background_image, (0, 0))
            self.screen.blit(victory_text, victory_text_rect)
            return_button.draw(self.screen)
            pygame.display.update()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == GAME_OVER:
                    if hasattr(event,'win') and event.win:
                        self.victory_menu()
                    else:
                        self.game_over_menu()
                    return

            self.screen.fill('black')
            self.camera_group.custom_draw(self.level.player)
            self.level.run()

            if self.level.check_victory():
                self.victory_menu()
                return
        
            pygame.display.update()
            self.clock.tick(FPS)

    def restart_game(self):
        print("Restarting Game...")
        self.level = None
        self.level_selection_menu()

    def return_menu(self):
        self.level = None
        main_menu()

    def game_over_menu(self):
        game_over_font = pygame.font.Font(UI_FONT, 40)
        game_over_text = game_over_font.render("Game Over!", True, 'red')
        game_over_text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        background_image = pygame.image.load("Assets/over back.jpg").convert()


        restart_button = Button((WIDTH // 3)+40, (HEIGHT // 2)-50, 250, 50, UI_BG_COLOR, TEXT_COLOR, game_over_font, "Restart",self.restart_game)
        return_button = Button((WIDTH // 3)-160, (HEIGHT // 2)+10, 650, 50, UI_BG_COLOR, TEXT_COLOR, game_over_font,"Return to Main Menu", self.return_menu)

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

            if background_image:
                self.screen.blit(background_image, (0, 0))

            self.screen.blit(game_over_text, game_over_text_rect)
            restart_button.draw(self.screen)
            return_button.draw(self.screen)
            pygame.display.update()

def handle_events(*buttons):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                button.handle_event(event)

def main_menu():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("RPG")

    font = pygame.font.Font(UI_FONT, 40)
    background_image = pygame.image.load("Assets/background.jpg").convert()
    start_button = Button((WIDTH // 2 - 100)-50, HEIGHT // 2 - 50, 350, 100, UI_BG_COLOR, TEXT_COLOR, font, "Start Game", start_game)
    quit_button = Button((WIDTH // 2 - 100)-50, HEIGHT // 2 + 50, 350, 100, UI_BG_COLOR, TEXT_COLOR, font, "Quit Game", quit_game)

    running = True
    while running:
        handle_events(start_button, quit_button)
        # for event in pygame.event.get():
        #     print("Event:", event)  # Debug
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         quit()

        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         print("Mouse clicked at:", event.pos)  # Debug
        #         start_button.handle_event(event)
        #         quit_button.handle_event(event)
        if background_image:
            screen.blit(background_image, (0, 0))

        start_button.draw(screen)
        quit_button.draw(screen)
        pygame.display.flip()
    pygame.quit()

def start_game():
    game = Game()
    game.run()

def quit_game():
    pygame.quit()
    quit()

if __name__ == "__main__":
    main_menu()
