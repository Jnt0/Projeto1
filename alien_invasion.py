import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game(): # Inicializa o pygame, as configurações e o objeto screen
    
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Cria uma espaçonave
    ship = Ship(screen)

    # Inicia o laço principal do jogo
    while True: 
        # Observa eventos de teclado e de mouse
        gf.check_events()

        # Redesenha a tela a cada passagem pelo laço
        # Deixa a tela mais recente visível
        gf.update_screen(ai_settings, screen, ship)

run_game()
