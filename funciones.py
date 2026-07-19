import pygame as pg
import variables as v

#Creamos una funcion para dibujar los elementos del juego
def dibujar():
    #Dibujamos el fondo de la pantalla
    v.pantalla.fill(v.FONDO)

    #Dibujamos los jugadores y la pelota
    pg.draw.rect(v.pantalla, v.AZUL, v.jugador1_rect)
    pg.draw.rect(v.pantalla, v.ROJO, v.jugador2_rect)
    pg.draw.rect(v.pantalla, v.BLANCO, v.pelota_rect)

    # Calculamos el rectángulo del texto del jugador 1 cada frame
    # para que quede centrado aunque el texto cambie de ancho (ej. "0" -> "10")
    Jugador1_texto_rect = v.Jugador1_texto.get_rect(centerx=200, top=20)

    # Lo mismo para el jugador 2, centrado en otro punto de la pantalla
    Jugador2_texto_rect = v.Jugador2_texto.get_rect(centerx=600, top=20)

    # Dibujamos los textos usando sus rectángulos centrados
    v.pantalla.blit(v.Jugador1_texto, Jugador1_texto_rect)
    v.pantalla.blit(v.Jugador2_texto, Jugador2_texto_rect)

def colision():
    # --- Jugador 1 (pala izquierda) ---
    # Comprobamos si la pelota colisiona con la pala del jugador 1
    # y además que la pelota se esté moviendo hacia la izquierda (< 0)
    # Esto evita que se detecte la colisión si la pelota va para el otro lado
    if v.pelota_rect.colliderect(v.jugador1_rect) and v.velociad_pelota_x < 0:
        
        # Calculamos cuánto se ha metido la pelota dentro de la pala en horizontal (eje X)
        # jugador1_rect.right es el borde derecho de la pala, que es por donde entra la pelota
        overlap_x = v.jugador1_rect.right - v.pelota_rect.left

        # Calculamos cuánto se ha metido la pelota por debajo del borde superior de la pala
        # Si este valor es pequeño, significa que la pelota está rozando la parte de arriba
        overlap_top = v.pelota_rect.bottom - v.jugador1_rect.top

        # Calculamos cuánto se ha metido la pelota por encima del borde inferior de la pala
        # Si este valor es pequeño, significa que la pelota está rozando la parte de abajo
        overlap_bottom = v.jugador1_rect.bottom - v.pelota_rect.top

        # Nos quedamos con el solapamiento vertical más pequeño de los dos (arriba o abajo)
        # Así sabemos por qué borde vertical está más "al límite" la pelota
        overlap_y = min(overlap_top, overlap_bottom)

        # Si el solapamiento vertical es menor que el horizontal, quiere decir que la pelota
        # entró rozando por arriba o por abajo, no de frente contra la pala
        if overlap_y < overlap_x:
            # Por lo tanto, solo invertimos la velocidad en Y (rebote como si fuera una pared)
            # y la velocidad en X se queda igual, para que la pelota siga de largo
            v.velociad_pelota_y *= -1
            v.sonido_golpe_pala.play()  # Reproducimos el sonido del golpe
        else:
            # Si no, es un golpe normal de frente contra la pala
            # Invertimos la velocidad en X para que la pelota rebote hacia el otro lado
            v.velociad_pelota_x *= -1
            # Colocamos la pelota justo pegada al borde derecho de la pala
            # Esto evita que la pelota se quede "atascada" dentro de la pala en el siguiente frame
            v.pelota_rect.left = v.jugador1_rect.right
            v.sonido_golpe_pala.play()  # Reproducimos el sonido del golpe

    # --- Jugador 2 (pala derecha) ---
    # Lo mismo que arriba pero para el jugador 2, comprobando que la pelota
    # se mueva hacia la derecha (> 0), porque es la única dirección desde la que puede chocar
    elif v.pelota_rect.colliderect(v.jugador2_rect) and v.velociad_pelota_x > 0:

        # Aquí la pelota entra por el borde izquierdo de la pala del jugador 2
        overlap_x = v.pelota_rect.right - v.jugador2_rect.left

        # Cuánto se mete la pelota por debajo del borde superior de la pala
        overlap_top = v.pelota_rect.bottom - v.jugador2_rect.top

        # Cuánto se mete la pelota por encima del borde inferior de la pala
        overlap_bottom = v.jugador2_rect.bottom - v.pelota_rect.top

        # Nos quedamos con el menor de los dos solapamientos verticales
        overlap_y = min(overlap_top, overlap_bottom)

        # Si el solapamiento vertical es menor, es que golpeó rozando arriba o abajo
        if overlap_y < overlap_x:
            # Rebote vertical, la X no cambia y la pelota sigue de largo
            v.velociad_pelota_y *= -1
            v.sonido_golpe_pala.play()  # Reproducimos el sonido del golpe
        else:
            # Golpe de frente normal, rebote horizontal
            v.velociad_pelota_x *= -1
            # Pegamos la pelota al borde izquierdo de la pala para que no se quede atascada
            v.pelota_rect.right = v.jugador2_rect.left
            v.sonido_golpe_pala.play()  # Reproducimos el sonido del golpe

def reset_game():
    v.pelota_rect.x = 400  # Reiniciamos la posición de la pelota
    v.pelota_rect.y = 300
    v.velociad_pelota_x *= -1  # Cambiamos la dirección de la pelota



def fuera_juego():
    #Comprobamos si la pelota sale de la pantalla por los lados

    if v.pelota_rect.x <= 0: 
        reset_game()
        v.puntaje_jugador2 += 1  # Incrementamos el puntaje del jugador 2
        v.Jugador2_texto = v.fuente.render("Jugador 2: " + str(v.puntaje_jugador2), True, (v.ROJO))
        v.sonido_punto.play()  # Reproducimos el sonido del punto

    elif v.pelota_rect.x >= 800:
        reset_game()  
        v.puntaje_jugador1 += 1  # Incrementamos el puntaje del jugador 1
        v.Jugador1_texto = v.fuente.render("Jugador 1: " + str(v.puntaje_jugador1), True, (v.AZUL))
        v.sonido_punto.play()  # Reproducimos el sonido del punto


def reset_all():
    v.pelota_rect.x = 400  # Reiniciamos la posición de la pelota
    v.pelota_rect.y = 300
    v.in_game = False  # Detenemos el juego

def ganador():
    #Comprobamos si alguno de los jugadores ha alcanzado el puntaje máximo
    if v.puntaje_jugador1 >= v.puntaje_maximo:
        print("¡Jugador 1 gana!")
        reset_all() 

    elif v.puntaje_jugador2 >= v.puntaje_maximo:
        print("¡Jugador 2 gana!")
        reset_all()

    


