from random import randrange, choice
from turtle import *
from freegames import square, vector

# Definir los colores que usaremos (sin usar el rojo)
colors = ['blue', 'green', 'yellow', 'purple', 'orange']

# Seleccionar colores aleatorios para la snake y la comida
snake_color = choice(colors)
food_color = choice([color for color in colors if color != snake_color])

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Inicializa la velocidad de la comida
food_speed = 400

def change(x, y):
    """Cambia la dirección de la serpiente."""
    aim.x = x
    aim.y = y

def inside(head):
    """Devuelve True si la cabeza está dentro de los límites."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():
    """Mueve la comida de manera aleatoria."""
    directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    move_direction = choice(directions)
    new_position = food + move_direction

    if inside(new_position):
        food.move(move_direction)
    
    # Mueve la comida otra vez después de 'food_speed' milisegundos
    ontimer(move_food, food_speed)

def move():
    """Mueve la serpiente hacia adelante un segmento."""
    global food_speed  # Declarar food_speed como global para modificarla
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        
        # Aumenta la velocidad de la comida (la hace más rápida)
        food_speed -= 20  # Disminuye la espera en 20 milisegundos

    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()

    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
move_food()  # Inicia el movimiento de la comida
done()
