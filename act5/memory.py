from random import shuffle
from turtle import *

from freegames import path

car = path('car.gif')
letras = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
    'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', '$', 
    '%', '&'
]
tiles = letras * 2  # Ahora tenemos 32 letras, multiplicadas por 2 para 64 tiles
state = {'mark': None, 'taps': 0}  # Añadimos un contador de taps al estado
hide = [True] * 64  # Lista que representa si los cuadros están ocultos o no

def square(x, y):
    """Dibuja un cuadrado blanco con borde negro en (x, y)."""
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
    """Convierte las coordenadas (x, y) en índice de tiles."""
    col = int((x + 200) // 50)
    row = int((y + 200) // 50)
    
    # Asegúrate de que las coordenadas estén dentro del rango válido
    if 0 <= col < 8 and 0 <= row < 8:
        return col + row * 8
    return -1  # Retorna un valor inválido si está fuera de los límites

def xy(count):
    """Convierte el índice de tiles en coordenadas (x, y)."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    """Actualiza la marca y los tiles ocultos basado en el tap."""
    spot = index(x, y)  # Calcula el índice del cuadro donde se hizo clic
    if spot == -1 or spot >= len(tiles):
        return  # Si el índice es inválido o fuera de rango, no hace nada

    mark = state['mark']  # Recupera la marca actual

    # Verifica que `mark` también esté dentro del rango antes de usarlo
    if mark is not None and (mark < 0 or mark >= len(tiles)):
        state['mark'] = None  # Resetea `mark` si está fuera de rango
        return

    state['taps'] += 1  # Incrementa el número de taps (clics)

    # Verifica si se debe actualizar la marca o si hay un par que destapar
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot  # Si no hay coincidencia, actualiza la marca
    else:
        hide[spot] = False  # Destapa el tile seleccionado
        hide[mark] = False  # Destapa el tile que coincidió
        state['mark'] = None  # Reinicia la marca

def draw():
    """Dibuja la imagen y los tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):  # Dibuja los tiles
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']  # Recupera la marca actual

    # Verifica que el índice de la marca esté dentro del rango antes de dibujar
    if mark is not None and 0 <= mark < len(tiles) and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y + 5)  # Ajusta para centrar la letra
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'), align='center')

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
