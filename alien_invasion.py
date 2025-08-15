import sys
import pygame
from MarcianoChuter.settings import Settings

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock().
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width , self.settings.screen_heigth)
        )
        pygame.display.set_caption("Invasion de Marcianekes")
        
        

    def run_game(self):
        #iniciamos el bucle del juego
        while True:
            #buscamos eventos de teclado y raton para salir del juego dentro de pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


            self.screen.fill(self.settings.bg_color)

            ##hacemos visible la ultima pantalla dibujada
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

