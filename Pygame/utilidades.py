import pygame

def colision(objeto1, objeto2):
    """Colisión precisa usando mask.overlap()"""
    mask1 = getattr(objeto1, "mask", None)
    mask2 = getattr(objeto2, "mask", None)

    if mask1 is None or mask2 is None:
        return False

    x1, y1 = objeto1.x, objeto1.y
    x2, y2 = objeto2.x, objeto2.y

    offset = (int(x2 - x1), int(y2 - y1))
    return mask1.overlap(mask2, offset) is not None

def dibujar_texto(pantalla, texto, tamaño, x, y, color=(255, 255, 255)):
    fuente = pygame.font.SysFont('Arial', tamaño)
    superficie_texto = fuente.render(texto, True, color)
    pantalla.blit(superficie_texto, (x, y))

from proyectil import Proyectil

def generar_proyectil(x, y, dir_x, dir_y, color, velocidad):
    return Proyectil(x, y, dir_x, dir_y, color=color, velocidad=velocidad)

def mostrar_menu(pantalla, ancho_pantalla, alto_pantalla):
    pantalla.fill((0, 0, 0))
    dibujar_texto(pantalla, "Juego: Presiona ESPACIO para iniciar", 30, ancho_pantalla // 2 - 200, alto_pantalla // 2)
    pygame.display.flip()
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    esperando = False

def mostrar_pausa(pantalla, ancho_pantalla, alto_pantalla):
    dibujar_texto(pantalla, "Pausa - Presiona P para continuar", 30, ancho_pantalla // 2 - 180, alto_pantalla // 2)
    pygame.display.flip()
    pausado = True
    while pausado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    pausado = False

def mostrar_mensaje_final(pantalla, mensaje, ancho_pantalla, alto_pantalla, color=(255, 255, 255)):
    pantalla.fill((0, 0, 0))
    dibujar_texto(pantalla, mensaje, 40, ancho_pantalla // 2 - 200, alto_pantalla // 2 - 20, color)
    dibujar_texto(pantalla, "Presiona ESC para salir", 30, ancho_pantalla // 2 - 150, alto_pantalla // 2 + 40)
    pygame.display.flip()
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    esperando = False
