import pygame as pg
import variables as v
import funciones as f

#Inicializar pygame
pg.init()

#Con esto cambiamos el titulo de la ventana 
# `icontitle`: (opcional) Especifica un título diferente para los iconos de la ventana. 
# Si se omite, `title` se usará para ambos.
#pygame.display.set_caption(title, icontitle=None)

#Actualiza toda la pantalla. 
# Esta función es utilizada para reflejar todos los cambios en la ventana del juego
#`pygame.display.flip()


#`pygame.display.update()`
#Actualiza partes de la pantalla, en lugar de toda la pantalla como `flip()`. 
# Puede ser más eficiente cuando solo necesitas actualizar una porción pequeña de la pantalla.

#Cambiamos el titulo de la ventana"
pg.display.set_caption(v.titulo)

#Cambiamos el icono de la ventana
pg.display.set_icon(v.icono)

#Creamos un bucle infinito para mantener la ventana abierta
while v.game:
    #Manejamos los eventos de la ventana
    for event in pg.event.get():
        #Si el evento es de tipo QUIT, cerramos el bucle
        if event.type == pg.QUIT:
            v.game = False

    if v.in_game:
        #Estado de las teclas
        teclas = pg.key.get_pressed()

        #Comprobamos el estado de las teclas
        if teclas[pg.K_w]:
            if v.jugador1_rect.y > 0:  # Evitar que el jugador salga de la pantalla
                v.jugador1_rect.y -= 5
        
        if teclas[pg.K_s]:
            if v.jugador1_rect.y < 600 - v.ALTO_JUGADOR:  # Evitar que el jugador salga de la pantalla, restamos la altura del jugador a la altura de la pantalla porque si no, el jugador se saldria de la pantalla
                v.jugador1_rect.y += 5

        if teclas[pg.K_UP]:
            if v.jugador2_rect.y > 0:  # Evitar que el jugador salga de la spantalla
                v.jugador2_rect.y -= 5

        if teclas[pg.K_DOWN]:
            if v.jugador2_rect.y < 600 - v.ALTO_JUGADOR:  # Evitar que el jugador salga de la pantalla
                v.jugador2_rect.y += 5

        #Modificamos la posición de la pelota
        v.pelota_rect.x += v.velociad_pelota_x
        v.pelota_rect.y += v.velociad_pelota_y

        #Hacemos una comprobacion para que la pelota rebote en los bordes de la pantalla de alto
        if v.pelota_rect.bottom >= 600 or v.pelota_rect.top <= 0: #Si la posición de la pelota es igual a 600 o 0, significa que ha llegado al borde de la pantalla
            v.velociad_pelota_y *= -1
            v.sonido_golpe_pared.play()  # Reproducimos el sonido del golpe
        
        f.colision()  # Llamamos a la función de colisión para comprobar si la pelota colisiona con los jugadores
        f.fuera_juego()  # Llamamos a la función de fuera de juego para comprobar si la pelota sale de la pantalla por los lados

        #Llamamos a la funcion de dibujar para dibujar los elementos del juego
        f.dibujar()

        f.ganador()  # Llamamos a la función de ganador para comprobar si algún jugador ha ganado

        #Actualizamos la pantalla para reflejar los cambios
        pg.display.flip()

        v.reloj.tick(60)  # Limitamos a 60 FPS

        

#Al salir del bucle, cerramos pygame y salimos del programa
pg.quit()
exit()





