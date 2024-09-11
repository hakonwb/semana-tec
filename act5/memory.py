from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2  # Lista de 64 tiles (32 duplicados para hacer pares)
state = {'mark': None, 'taps': 0}  # Se añade un contador de taps al estado
hide = [True] * 64  # Lista que representa si los cuadros están ocultos o no


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)  # Calcula el índice del cuadro donde se hizo clic
    mark = state['mark']  # Recupera la marca actual

    state['taps'] += 1  # Incrementa el número de taps (clics)

    # Verifica si se debe actualizar la marca o si hay un par que destapar
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot  # Si no hay coincidencia, actualiza la marca
    else:
        hide[spot] = False  # Destapa el tile seleccionado
        hide[mark] = False  # Destapa el tile que coincidió
        state['mark'] = None  # Reinicia la marca


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):  # Dibuja los tiles
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']  # Recupera la marca actual

    # Dibuja el número del tile si está marcado y aún está oculto
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    # Dibuja el número de taps (clics) en la esquina inferior izquierda
    up()
    goto(-180, -200)
    color('black')
    write(f'Taps: {state["taps"]}', font=('Arial', 15, 'normal'))

    # Detecta si todos los tiles han sido destapados
    if all(not hidden for hidden in hide):  # Verifica si todos los cuadros están destapados
        goto(0, 0)
        color('red')
        write('¡Juego completado!', align='center', font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)  # Llama a la función de dibujar cada 100 milisegundos


# Mezcla las piezas y configura la pantalla
shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)  # Asigna la función tap a los clics en la pantalla
draw()
done()
