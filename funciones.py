import sys
import random

import pygame as pg
import variables as v

# Una Surface es un objeto gráfico de Pygame que representa una imagen o área de dibujo. 
# La pantalla, las imágenes cargadas y los textos renderizados son todos Surface. 
# Luego usas blit() para copiar una Surface sobre otra.


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
    v.cpu_target_offset = random.randint(-v.cpu_error, v.cpu_error)



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


def reset_all(jugador): # Funcion para resetear la posicion y determinar el mensaje final
    v.pelota_rect.x = 400  # Reiniciamos la posición de la pelota
    v.pelota_rect.y = 300
    v.jugador1_rect.y = 250
    v.jugador2_rect.y = 250
    v.in_game = False  # Detenemos el juego
    v.menu_mode = "end"
    v.final_message = jugador


def ganador(): # Funcion para ver quien ha ganado el juegp
    #Comprobamos si alguno de los jugadores ha alcanzado el puntaje máximo
    if v.puntaje_jugador1 >= v.puntaje_maximo:
        reset_all("¡Jugador 1 gana!") #Llamamos a la funcion anterior con el texto indicado

    elif v.puntaje_jugador2 >= v.puntaje_maximo:
        reset_all("¡Jugador 2 gana!")

def menuInicial(eventos): # Funcion para generar el menu inicial
    v.pantalla.fill(v.NEGRO)  # Limpiamos

    titulo = v.fuente.render("PONG", True, v.BLANCO) # Titulo
    icono_escalado = pg.transform.scale(v.icono, (titulo.get_height(), titulo.get_height())) # Escalamos la imagen 
    v.pantalla.blit(titulo, titulo.get_rect(center=(400, 120))) # Lo pintamos en una posicion indicada
    v.pantalla.blit(icono_escalado, icono_escalado.get_rect(center=(470, 120)))

    # Creamos rects con medidas, height y witdh mas la posicion
    local = pg.Rect(120, 250, 260, 90)
    cpu = pg.Rect(420, 250, 260, 90)
    config = pg.Rect(280, 370, 240, 70)

    # Lo pintamos en pantalla dando border_radius
    pg.draw.rect(v.pantalla, v.AZUL, local, border_radius=20)
    pg.draw.rect(v.pantalla, v.ROJO, cpu, border_radius=20)
    pg.draw.rect(v.pantalla, v.BLANCO, config, 3, border_radius=20) # El 3 es el grosor del borde

    # Creamos los textos de los rects 
    texto_local = v.fuente.render("2 Jugadores", True, v.BLANCO)
    texto_cpu = v.fuente.render("CPU", True, v.BLANCO)
    texto_config = v.fuente.render("Puntaje", True, v.BLANCO)

    # Pintamos como antes pero en el center del rect creado anteriormente
    v.pantalla.blit(texto_local, texto_local.get_rect(center=local.center))
    v.pantalla.blit(texto_cpu, texto_cpu.get_rect(center=cpu.center))
    v.pantalla.blit(texto_config, texto_config.get_rect(center=config.center))
    
    instruccion = v.fuente.render("Esc: Salir", True, v.BLANCO)
    v.pantalla.blit(instruccion, instruccion.get_rect(center=(400, 520)))

    pg.display.flip() # Actualizamos pantalla

    # Recorremos eventos
    for event in eventos:
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE: # Si es un evento de teclado y la tecla pulsada es escape
            v.game = False # El bucle de main termina
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1: # Si presiona un boton del raton y es el 1, es decir el izquierdo
            if local.collidepoint(event.pos): # Comprobamos si esta dentro de local (El boton creado antes)
                v.cpu_mode = False # Desactivamos la CPU
                v.in_game = True # Empezamos el juego
            elif cpu.collidepoint(event.pos): # Lo mismo pero con el boton CPU
                v.cpu_mode = True
                v.in_game = True
            elif config.collidepoint(event.pos): # Si el clic esta dentro de config, el menu_mode cambia a input
                v.menu_mode = "input"


def menuSeleccion(eventos):
    v.pantalla.fill(v.NEGRO)

    titulo = v.fuente.render("Puntaje máximo", True, v.BLANCO)
    v.pantalla.blit(titulo, titulo.get_rect(center=(400, 120))) # Pegamos a la pantalla el titulo, como hacemos get_rect nos algo asi: <rect(0, 0, 220, 45)>, al escribri center lo centra directamente desde el centro
    # y no des de la esquina superior izquierda, pasa a ser: <rect(290, 98, 220, 45)> para que quede en ese centro.

    pg.draw.rect(v.pantalla, v.BLANCO, v.input_box, 3, border_radius=12)
    texto = v.fuente_pequena.render(v.input_text, True, v.BLANCO)
    v.pantalla.blit(texto, (v.input_box.x + 15, v.input_box.y + 15))

    etiqueta = v.fuente.render("Presiona Enter para guardar", True, v.BLANCO)
    v.pantalla.blit(etiqueta, etiqueta.get_rect(center=(400, 500)))

    if v.input_active:
        cursor = v.fuente.render("|", True, v.BLANCO)
        v.pantalla.blit(cursor, (v.input_box.x + 15 + texto.get_width() + 5, v.input_box.y + 10))

    pg.display.flip()

    for event in eventos:
        if event.type == pg.QUIT:
            v.game = False
        elif event.type == pg.KEYDOWN: # Si pulsa una tecla de teclado
            if event.key == pg.K_ESCAPE: # Miramos si es escape
                v.menu_mode = "main"
                v.input_active = False
            elif event.key == pg.K_RETURN and v.input_active: # Si la key es Enter y input esta activo
                if v.input_text.isdigit() and v.input_text != "": # Si el input text es un digito y es diferente a vacio
                    v.puntaje_maximo = int(v.input_text) # Cambiamos el puntaje por lo que ponga en input 
                v.menu_mode = "main"
                v.input_active = False # Y cambiamos el input active a false
            elif v.input_active: # Si no le ha dado el enter pero input esta activo
                if event.key == pg.K_BACKSPACE: # Si presiona la tecla de borrar
                    v.input_text = v.input_text[:-1] # Le borramos el ultimo digito a input text
                elif event.unicode.isdigit(): # Si unicode que es lo que se escribe, es decir ahi se guarda la tecla que pulsas, si es digito
                    v.input_text += event.unicode # A input le sumamos la tecla
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1: # Si lo que habia pulsado no era una tecla y era con el raton, clic izquierdo porque hemos puesto 1
            if v.input_box.collidepoint(event.pos): # Si esta en el rango del boton
                v.input_active = True # Estamos en el input
            else:
                v.input_active = False # Si no, no


def menuFinal(eventos):
    v.pantalla.fill((20, 24, 40))

    titulo = v.fuente.render("FIN DEL JUEGO", True, v.BLANCO)
    mensaje = v.fuente.render(v.final_message, True, v.BLANCO)
    v.pantalla.blit(titulo, titulo.get_rect(center=(400, 110)))
    v.pantalla.blit(mensaje, mensaje.get_rect(center=(400, 180)))

    boton_reiniciar = pg.Rect(80, 320, 300, 100)
    boton_menu = pg.Rect(420, 320, 300, 100)

    pg.draw.rect(v.pantalla, v.AZUL, boton_reiniciar, border_radius=24)
    pg.draw.rect(v.pantalla, v.ROJO, boton_menu, border_radius=24)

    texto_reiniciar = v.fuente.render("Volver a jugar", True, v.BLANCO)
    texto_menu = v.fuente.render("Menú inicial", True, v.BLANCO)

    v.pantalla.blit(texto_reiniciar, texto_reiniciar.get_rect(center=boton_reiniciar.center))
    v.pantalla.blit(texto_menu, texto_menu.get_rect(center=boton_menu.center))

    instruccion = v.fuente.render("Esc: Salir", True, v.BLANCO)
    v.pantalla.blit(instruccion, instruccion.get_rect(center=(400, 520)))

    pg.display.flip()

    for event in eventos:
        if event.type == pg.QUIT:
            v.game = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            v.game = False
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if boton_reiniciar.collidepoint(event.pos):
                resetMenus()
                v.in_game = True
                v.menu_mode = "main"
            elif boton_menu.collidepoint(event.pos):
                resetMenus()
                v.menu_mode = "main"
                v.in_game = False

def menuPausa(): # Cada vez que ejecutemos esta funcion pausa es true y se inciia un bucle diferente al del main
    v.pausa = True
    while v.pausa:

        #Manejamos los eventos de la ventana
        eventos = pg.event.get()
        for event in eventos:
            #Si el evento es de tipo QUIT, cerramos el bucle
            if event.type == pg.QUIT:
                v.game = False
                v.pausa = False

        v.pantalla.fill(v.NEGRO)  # Limpiamos
        titulo = v.fuente.render("PAUSA", True, v.BLANCO)
        v.pantalla.blit(titulo, titulo.get_rect(center=(400, 120)))

        continuar = pg.Rect(120, 250, 260, 90)
        reiniciar = pg.Rect(420, 250, 260, 90)
        menu = pg.Rect(230, 370, 340, 90)

        pg.draw.rect(v.pantalla, v.AZUL, continuar, border_radius=20)
        pg.draw.rect(v.pantalla, v.ROJO, reiniciar, border_radius=20)
        pg.draw.rect(v.pantalla, v.BLANCO, menu, 3, border_radius=20)

        texto_continuar = v.fuente.render("CONTINUAR", True, v.BLANCO)
        texto_reiniciar = v.fuente.render("REINICIAR", True, v.BLANCO)
        texto_menu = v.fuente.render("Volver al menu", True, v.BLANCO)

        v.pantalla.blit(texto_continuar, texto_continuar.get_rect(center=continuar.center))
        v.pantalla.blit(texto_reiniciar, texto_reiniciar.get_rect(center=reiniciar.center))
        v.pantalla.blit(texto_menu, texto_menu.get_rect(center=menu.center))

        instruccion = v.fuente.render("Esc: Salir", True, v.BLANCO)
        v.pantalla.blit(instruccion, instruccion.get_rect(center=(400, 520)))

        pg.display.flip()
        

        for event in eventos:
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                v.game = False
                v.pausa = False
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if continuar.collidepoint(event.pos):
                    v.pausa = False
                elif reiniciar.collidepoint(event.pos):
                    resetMenus()
                    v.pausa = False
                elif menu.collidepoint(event.pos):
                    resetMenus()
                    v.in_game = False
                    v.menu_mode = "main"
                    v.pausa = False
def resetMenus():
    v.puntaje_jugador1 = 0
    v.puntaje_jugador2 = 0
    v.Jugador1_texto = v.fuente.render("Jugador 1: 0", True, v.AZUL)
    v.Jugador2_texto = v.fuente.render("Jugador 2: 0", True, v.ROJO)
    v.pelota_rect.center = (400, 300)
    v.velociad_pelota_x = 4
    v.velociad_pelota_y = 4
