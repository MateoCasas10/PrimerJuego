import pygame

class Proyectil:
    def __init__(self, x, y, dir_x, dir_y, color, velocidad):
        self.x = x
        self.y = y
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.color = color
        self.velocidad = velocidad
        self.radio = 5
        self.imagen = pygame.Surface((self.radio * 2, self.radio * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.imagen, self.color, (self.radio, self.radio), self.radio)
        self.mask = pygame.mask.from_surface(self.imagen)

    def mover(self):
        self.x += self.dir_x * self.velocidad
        self.y += self.dir_y * self.velocidad

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))

    def fuera_de_pantalla(self, alto, ancho):
        return self.x < 0 or self.x > ancho or self.y < 0 or self.y > alto

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.radio * 2, self.radio * 2)
