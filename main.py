import pygame as pg
import variables as v

#Inicializar pygame
pg.init()

#Con esto cambiamos el titulo de la ventana 
# `icontitle`: (opcional) Especifica un título diferente para los iconos de la ventana. 
# Si se omite, `title` se usará para ambos.
#pygame.display.set_caption(title, icontitle=None)

#Actualiza toda la pantalla. 
# Esta función es utilizada para reflejar todos los cambios en la ventana del juego
#`pygame.display.flip()`


#`pygame.display.update()`
#Actualiza partes de la pantalla, en lugar de toda la pantalla como `flip()`. 
# Puede ser más eficiente cuando solo necesitas actualizar una porción pequeña de la pantalla.

#Cambiamos el titulo de la ventana"
pg.display.set_caption(v.titulo)

#Cambiamos el icono de la ventana
pg.display.set_icon(v.icono)


#Creamos una funcion para dibujar los elementos del juego
def dibujar():
    #Dibujamos el fondo de la pantalla
    v.pantalla.fill(v.FONDO)

    #Dibujamos los jugadores y la pelota
    pg.draw.rect(v.pantalla, v.AZUL, v.jugador1)
    pg.draw.rect(v.pantalla, v.ROJO, v.jugador2)
    pg.draw.rect(v.pantalla, v.BLANCO, v.pelota)


#Creamos un bucle infinito para mantener la ventana abierta
while v.game:
    #Manejamos los eventos de la ventana
    for event in pg.event.get():
        #Si el evento es de tipo QUIT, cerramos el bucle
        if event.type == pg.QUIT:
            v.game = False
    
    #Llamamos a la funcion de dibujar para dibujar los elementos del juego
    dibujar()

    #Actualizamos la pantalla para reflejar los cambios
    pg.display.flip()

    v.reloj.tick(60)  # Limitamos a 60 FPS

    

#Al salir del bucle, cerramos pygame y salimos del programa
pg.quit()
exit()





