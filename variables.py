import pygame as pg

#Variable para controlar el bucle del juego
game = True

#Variable para controlar el tiempo del juego
reloj = pg.time.Clock()

#Configurar la pantalla
pantalla = pg.display.set_mode((800,600))


#Icono de la ventana
icono = pg.image.load("pong.png")

#Titulo de la ventana
titulo = "PONG"

#COLORES
#Definimos los colores que vamos a usar en el juego
BLANCO = (255,255,255)
FONDO = (150, 200, 170)
AZUL = (70,130,180)
ROJO = (200,70,90)

#Cordenadas y tamaños 
jugador1_x = 50
jugador1_y = 250

jugador2_x = 750
jugador2_y = 250 

ANCHO_JUGADOR = 30
ALTO_JUGADOR = 100

#Cordenadas y tamaño de la pelota
pelota_x = 400
pelota_y = 300
ANCHO_PELOTA = 10
ALTO_PELOTA = 10

#Elementos del juego
jugador1 = pg.Rect(jugador1_x, jugador1_y, ANCHO_JUGADOR, ALTO_JUGADOR)
jugador2 = pg.Rect(jugador2_x, jugador2_y, ANCHO_JUGADOR, ALTO_JUGADOR)
pelota = pg.Rect(pelota_x, pelota_y, ANCHO_PELOTA, ALTO_PELOTA)

#Estado de las teclas
teclas = pg.key.get_pressed()