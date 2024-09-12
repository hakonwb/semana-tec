from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        #Se aumenta la velocidad del proyectil (de dividir entre 25 a 10)
        speed.x = (x + 200) / 10
        speed.y = (y + 200) / 10


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)
    #Aumentar la velocidad de los objetivos
    for target in targets:
        target.x -= 3 #(de 0.5 a 3)

    if inside(ball):
        speed.y -= 0.35 #(de 0.35 a 0.8, mayor gravedad)
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        #Si la cannon ball no ha golpeado un objetivo, se añade a la lista de los targets
        if abs(target-ball) > 20:
            targets.append(target)
        #objetivos que han salido de la pantalla
        if not inside(target):
            target.x = 200  # Reposiciona en el borde derecho pero sigue en la lista

    draw()
    ontimer(move, 15) #frecuencia de actualizacion aumentada (50-30)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
