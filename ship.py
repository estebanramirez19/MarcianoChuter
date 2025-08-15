import pygame

class Ship:

    def __init__(self, ai_game):
        #se inicializa la nave y su posicion inicial
        self.screen = ai_game.screen
        self.settings = ai_game.setings
        self.screen_rect = ai_game.screen.get_rect()

        #cargar la imagen de la nave y obtener su rect
        self.image = pygame.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()

        #esto coloca la imagen del la nueva nave inicialmente en el centro
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        #bandera de movimiento
        self.moving_right = False
        self.moving_left = False


    def update(self):
        if self.moving_right:
            self.rect.x += self.settings.ship_speed

        if self.moving_left:
            self.rect.x -= self.settings.ship_speed

    def blitme(self):
        #dibuja la nave en su ubicacion actual
        self.screen.blit(self.image, self.rect)