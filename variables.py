from tkinter import font
import pygame as pg
from pathlib import Path
pg.init()  


#Variable para controlar el bucle del juego
game = True

#Variable para controlar el tiempo del juego
reloj = pg.time.Clock()

#Configurar la pantalla
pantalla = pg.display.set_mode((800,600))


#Icono de la ventana

BASE_DIR = Path(__file__).resolve().parent
icono = pg.image.load(BASE_DIR / "assets" / "pong.png")

#Titulo de la ventana
titulo = "PONG"

#COLORES
#Definimos los colores que vamos a usar en el juego
BLANCO = (255,255,255)
FONDO = (150, 200, 170)
AZUL = (70,130,180)
ROJO = (200,70,90)
NEGRO = (0,0,0)

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
velociad_pelota_x = 4
velociad_pelota_y = 4


#Elementos del juego
# Estas son las posiciones iniciales. Una vez el rect se crea, su posición actual
# se accede con .x y .y sobre el propio objeto.
jugador1_rect = pg.Rect(jugador1_x, jugador1_y, ANCHO_JUGADOR, ALTO_JUGADOR)
jugador2_rect = pg.Rect(jugador2_x, jugador2_y, ANCHO_JUGADOR, ALTO_JUGADOR)
pelota_rect = pg.Rect(pelota_x, pelota_y, ANCHO_PELOTA, ALTO_PELOTA)



#Elementos del puntaje
pg.font.init()

puntaje_jugador1 = 0
puntaje_jugador2 = 0
puntaje_maximo = 2  # Puntaje máximo para ganar el juego

# Configurar la fuente
fuente = pg.font.Font(None, 48)
fuente_pequena = pg.font.Font(None, 34)

# Crear una superficie con el texto
Jugador1_texto = fuente.render("Jugador 1: " + str(puntaje_jugador1), True, (AZUL))
Jugador2_texto = fuente.render("Jugador 2: " + str(puntaje_jugador2), True, (ROJO))



#Sonidos
#El objeto `Sound()` en Pygame se utiliza para cargar y manejar efectos de sonido. 
#Puedes crear un objeto `Sound()` desde un archivo de audio y luego reproducirlo, detenerlo o modificar sus propiedades como el volumen.
sonido_golpe_pala = pg.mixer.Sound("assets/golpe_paleta.mp3")
sonido_golpe_pared = pg.mixer.Sound("assets/golpe_pared.mp3")
sonido_punto = pg.mixer.Sound("assets/punto.mp3")

sonido_golpe_pala.set_volume(0.5)  # Ajusta el volumen del sonido (0.0 a 1.0)
sonido_golpe_pared.set_volume(0.5)
sonido_punto.set_volume(0.3)


in_game = False  # Variable para controlar si el juego está en curso o no (inicio en menú)


#CPU Mode
cpu_mode = False  # Si es True, el jugador 2 se mueve automáticamente
cpu_vel = 3  # Velocidad de la CPU cuando sigue la pelota
cpu_reaccion = 20  # Zona de tolerancia para que la CPU no reaccione instantáneamente
cpu_error = 40  # Desviación aleatoria en el objetivo de la CPU
cpu_target_offset = 0  # Offset actual que la CPU usa para añadir imprecisión

# Menú y entrada de texto
menu_mode = "main"  # "main" para menú inicial, "input" para la pantalla de texto, "end" para menú final
input_box = pg.Rect(240, 420, 320, 60)
input_text = str(puntaje_maximo)
input_active = False
final_message = ""  # Texto que mostrará el menú final


#Menu pausa
pausa = False
