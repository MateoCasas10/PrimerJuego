import pygame
import random

class Enemigo:
    def __init__(self, x, y, ancho, alto, ruta_imagen):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.velocidad = 3
        self.vida = 100
        self.imagen = pygame.image.load(ruta_imagen).convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.mask = pygame.mask.from_surface(self.imagen)
        self.direccion = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        self.cambio_direccion_tiempo = pygame.time.get_ticks()

    def mover(self, ancho_pantalla, alto_pantalla):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.cambio_direccion_tiempo > 2000:
            self.direccion = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
            self.cambio_direccion_tiempo = tiempo_actual

        nueva_x = self.x + self.direccion[0] * self.velocidad
        nueva_y = self.y + self.direccion[1] * self.velocidad

        if 0 <= nueva_x <= ancho_pantalla - self.ancho:
            self.x = nueva_x
        if 0 <= nueva_y <= alto_pantalla - self.alto:
            self.y = nueva_y

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.ancho, self.alto)
