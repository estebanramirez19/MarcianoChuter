import pygame

class Ship:

    def __init__(self, ai_game):
        #se inicializa la nave y su posicion inicial
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #cargar la imagen de la nave y obtener su rect
        self.image = pygame.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()

        #esto coloca la imagen del la nueva nave inicialmente en el centro
        self.rect.midbottom = self.screen_rect.midbottom

        #bandera de movimiento
        self.moving_right = False

    def update(self):
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        #dibuja la nave en su ubicacion actual
        self.screen.blit(self.image, self.rect)