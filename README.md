# Pong Game Python

Una recreación del clásico Pong desarrollada con Python y Pygame.

El proyecto incluye:

- Modo 2 jugadores.
- Modo jugador contra CPU.
- Menú principal interactivo.
- Configuración del puntaje máximo antes de comenzar la partida.
- Sistema de puntuación.
- Interfaz sencilla y fácil de usar.

## Capturas

### Menú principal

....
### Partida

....

### Pantalla de victoria

....



---

## Requisitos

Antes de ejecutar el proyecto necesitas tener instalado:

- Python 3.10 o superior
- Pygame

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Erik-CR46/Pong-Game-Python.git
```

### 2. Entrar en el directorio

```bash
cd Pong-Game-Python
```

### 3. Instalar dependencias

```bash
pip install pygame
```

También puedes usar:

```bash
pip install -r requirements.txt
```

---

## Cómo ejecutar el juego

Desde la carpeta raíz del proyecto:

```bash
python main.py
```


---

## Controles

### Menú principal

- **Clic izquierdo** para seleccionar una opción.
- **ESC** para salir o volver atrás.

### Partida local (2 jugadores)

**Jugador 1**

- W → Arriba
- S → Abajo

**Jugador 2**

- Flecha ↑ → Arriba
- Flecha ↓ → Abajo

### Configuración de puntaje

- Haz clic sobre la caja de texto.
- Introduce el puntaje máximo deseado.
- Pulsa **Enter** para guardar.
- Pulsa **ESC** para volver al menú principal.

---

## Estructura del proyecto

```text
Pong-Game-Python/
│
├── main.py
├── variables.py
├── funciones.py
├── assets/
│   ├── icono.png
│   └── golpe_paleta.mp3
│   └── golpe_pared.mp3
│   └── punto.mp3
│
└── README.md

---

## Características implementadas

- Menú principal.
- Selección entre CPU o 2 jugadores.
- Configuración dinámica del puntaje máximo.
- Detección de colisiones.
- Sistema de reinicio tras anotar.
- Marcador en tiempo real.
- Interfaz realizada con Pygame.

---

## Tecnologías utilizadas

- Python
- Pygame

---

## Posibles mejoras futuras

- Sistema de dificultad para la CPU.
- Modo pantalla completa.
- Mejoras visuales y animaciones.

---

## Autor

**Erik Catalán Rodríguez**

GitHub:
https://github.com/Erik-CR46

---

## Licencia

Este proyecto ha sido desarrollado con fines educativos y de aprendizaje.
