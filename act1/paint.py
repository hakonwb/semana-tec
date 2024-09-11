
#Librerias
from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def draw_circle(start, end):
    "Draw circle from start to end."
    # Se mueve el cursor de turtle a la posición inicial (start.x, start.y) con up() y goto() para no dibujar durante el movimiento.
    up()
    goto(start.x, start.y)
    down()

    # Calcular el radio como la distancia entre los puntos start y end
    radius = ((end.x - start.x)**2 + (end.y - start.y)**2)**0.5

    # Posicionar la tortuga correctamente
    up()
    goto(start.x, start.y - radius)
    down()

    # Dibujar el círculo con el radio calculado y rellenar
    begin_fill()
    circle(radius)
    end_fill()
    # terminamos de crear y rellenar el circulo con el color actual
def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x,start.y)
    down()
    begin_fill()
    #Dibujar rectangulo
    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()

def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    #For que dibuja un triángulo
    for count in range(3):
        forward(end.x-start.x)
        left(120)
    end_fill()

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
#añadimos el color amarillo con la tecla "Y"
onkey(lambda: color('yellow'), 'y')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', draw_circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
