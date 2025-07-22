import pygame
import random
import os
from jugador import Jugador
from enemigo import Enemigo
from proyectil import Proyectil
from utilidades import (
    dibujar_texto, generar_proyectil,
    mostrar_menu, mostrar_pausa, mostrar_mensaje_final
)

class GameManager:
    def __init__(self, pantalla, ancho, alto):
        self.pantalla = pantalla
        self.ancho = ancho
        self.alto = alto
        self.clock = pygame.time.Clock()
        self.negro = (0, 0, 0)
        self.amarillo = (255, 255, 0)
        self.morado = (128, 0, 128)

        ruta = os.path.dirname(__file__)
        ruta_jugador = os.path.join(ruta, "imagenes", "jugador.png")
        ruta_enemigo = os.path.join(ruta, "imagenes", "enemigo.png")

        ruta_fondo = os.path.join(ruta,"imagenes", "fondo.png")
        self.fondo = pygame.image.load(ruta_fondo).convert()
        self.fondo = pygame.transform.scale(self.fondo, (self.ancho, self.alto))

        self.player = Jugador(x=100, y=300, ancho=250, alto=200, ruta_imagen=ruta_jugador)
        self.enemy = Enemigo(x=600, y=300, ancho=200, alto=150, ruta_imagen=ruta_enemigo)
        self.proyectiles_player = []
        self.proyectiles_enemigo = []

        self.tiempo_disparo_enemigo = pygame.time.get_ticks()
        self.intervalo_disparo = random.randint(1000, 1500)

        

    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    mostrar_pausa(self.pantalla, self.ancho, self.alto)
                if evento.key == pygame.K_SPACE:
                    centro_x = self.player.rect.centerx
                    centro_y = self.player.rect.top
                    proyectil = generar_proyectil(
                        centro_x, centro_y, 0, -1, self.amarillo, 5
                    )
                    self.proyectiles_player.append(proyectil)

    def actualizar_proyectiles(self):
        for p in self.proyectiles_player[:]:
            p.mover()
            p.dibujar(self.pantalla)
            if p.fuera_de_pantalla(self.alto, self.ancho):
                self.proyectiles_player.remove(p)

        for p in self.proyectiles_enemigo[:]:
            p.mover()
            p.dibujar(self.pantalla)
            if p.fuera_de_pantalla(self.alto, self.ancho):
                self.proyectiles_enemigo.remove(p)

    def colisiona_mask(self, objeto1, objeto2):
        offset_x = objeto2.rect.x - objeto1.rect.x
        offset_y = objeto2.rect.y - objeto1.rect.y
        return objeto1.mask.overlap(objeto2.mask, (offset_x, offset_y)) is not None

    def verificar_colisiones(self):
        for p in self.proyectiles_player[:]:
            if self.colisiona_mask(p, self.enemy):
                self.enemy.vida -= 5
                self.proyectiles_player.remove(p)

        for p in self.proyectiles_enemigo[:]:
            if self.colisiona_mask(p, self.player):
                self.player.vida -= 5
                self.proyectiles_enemigo.remove(p)

        if self.colisiona_mask(self.player, self.enemy):
            self.player.vida -= 15

    def disparo_aleatorio_enemigo(self):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_disparo_enemigo > self.intervalo_disparo:
            centro_x = self.enemy.rect.centerx
            centro_y = self.enemy.rect.centery
            dir_x, dir_y = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
            proyectil = generar_proyectil(centro_x, centro_y, dir_x, dir_y, self.morado, 2)
            self.proyectiles_enemigo.append(proyectil)
            self.tiempo_disparo_enemigo = tiempo_actual
            self.intervalo_disparo = random.randint(1000, 1500)

    def mostrar_hud(self):
        largo_barra = 200
        alto_barra = 20
        margen_izquierdo = 20
        margen_superior = 20

        proporcion_jugador = self.player.vida / 100
        pygame.draw.rect(self.pantalla, (255, 0, 0), (margen_izquierdo, margen_superior, largo_barra, alto_barra))
        pygame.draw.rect(self.pantalla, (0, 0, 255), (margen_izquierdo, margen_superior, largo_barra * proporcion_jugador, alto_barra))
        dibujar_texto(self.pantalla, f"Jugador: {self.player.vida}", 18, margen_izquierdo, margen_superior - 20)

        proporcion_enemigo = self.enemy.vida / 100
        barra_y_enemigo = margen_superior + alto_barra + 25
        pygame.draw.rect(self.pantalla, (255, 0, 0), (margen_izquierdo, barra_y_enemigo, largo_barra, alto_barra))
        pygame.draw.rect(self.pantalla, (128, 0, 128), (margen_izquierdo, barra_y_enemigo, largo_barra * proporcion_enemigo, alto_barra))
        dibujar_texto(self.pantalla, f"Enemigo: {self.enemy.vida}", 18, margen_izquierdo, barra_y_enemigo - 20)

    def jugar(self):
        mostrar_menu(self.pantalla, self.ancho, self.alto)
        corriendo = True
        while corriendo:
            self.pantalla.blit(self.fondo, (0,0))
            self.manejar_eventos()
            self.player.mover(self.ancho, self.alto)
            self.enemy.mover(self.ancho, self.alto)
            self.player.dibujar(self.pantalla)
            self.enemy.dibujar(self.pantalla)
            self.actualizar_proyectiles()
            self.verificar_colisiones()
            self.disparo_aleatorio_enemigo()
            self.mostrar_hud()

            if self.enemy.vida <= 0:
                mostrar_mensaje_final(self.pantalla, "¡Victoria! Has vencido al enemigo.", self.ancho, self.alto)
                corriendo = False
            elif self.player.vida <= 0:
                mostrar_mensaje_final(self.pantalla, "Derrota... El enemigo te ha vencido.", self.ancho, self.alto)
                corriendo = False

            pygame.display.update()
            self.clock.tick(60)
