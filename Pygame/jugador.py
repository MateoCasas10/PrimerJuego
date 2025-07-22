import pygame

class Jugador:
    def __init__(self, x, y, ancho, alto, ruta_imagen):
        self.x = x
        self.y = y
        self.velocidad = 5
        self.vida = 100

        # Cargar imagen y generar máscara
        self.imagen_original = pygame.image.load(ruta_imagen).convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen_original, (ancho, alto))
        self.mascara = pygame.mask.from_surface(self.imagen)
        self.ancho = self.imagen.get_width()
        self.alto = self.imagen.get_height()
    def mover(self, ancho_pantalla, alto_pantalla):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.x = max(0, self.x - self.velocidad)
        if teclas[pygame.K_RIGHT]:
            self.x = min(ancho_pantalla - self.ancho, self.x + self.velocidad)
        if teclas[pygame.K_UP]:
            self.y = max(0, self.y - self.velocidad)
        if teclas[pygame.K_DOWN]:
            self.y = min(alto_pantalla - self.alto, self.y + self.velocidad)


    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.ancho, self.alto)

    @property
    def mask(self):
        return self.mascara

    def obtener_posicion(self):
        return (self.x, self.y)
