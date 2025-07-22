import pygame
from game_manager import GameManager

pygame.init()
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego: Jugador vs Enemigo")

juego = GameManager(pantalla, ancho, alto)
juego.jugar()
 