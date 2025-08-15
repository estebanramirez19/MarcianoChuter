import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width , self.settings.screen_heigth)
        )
        pygame.display.set_caption("Invasion de Marcianekes")

        self.ship = Ship(self)
        
    ## creamos dos funciones _check_events y _update_screen para que run game no este tan poblado de codigo

    def _check_events(self):
        # buscamos eventos de teclado y raton para salir del juego dentro de pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False


    def _update_screen(self): ## encargado de la configuracion de la pantalla
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            ## hacemos visible la ultima pantalla dibujada
            pygame.display.flip()

    def run_game(self):
        #iniciamos el bucle del juego
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

