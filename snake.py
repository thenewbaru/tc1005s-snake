"""

Juego de la Serpiente (Snake)
Input: Teclas de dirección (Up, Down, Left, Right) para mover la serpiente.
Process:
  - Actualiza la posición de la serpiente cada 100ms.
  - Verifica colisiones con los bordes o con su propio cuerpo.
  - Si come la comida, crece; si no, avanza.
  - Mueve la comida de forma aleatoria un paso a la vez.
Output: Renderizado gráfico del juego en la ventana de Turtle.
"""

from random import choice, randrange, sample
from turtle import (
    clear, done, hideturtle, listen, onkey,
    ontimer, setup, tracer, update,
)
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

colors = ['blue', 'purple', 'orange', 'yellow', 'pink']
snake_color, food_color = sample(colors, 2)


def change(x, y):
    """
    Cambia la dirección de la serpiente.
    Input: Coordenadas x, y de la nueva dirección.
    Process: Asigna las nuevas coordenadas al vector 'aim'.
    Output: Ninguno.
    """
    aim.x = x
    aim.y = y


def inside(head):
    """
    Verifica si la cabeza está dentro de los límites.
    Input: Vector 'head' con las coordenadas actuales.
    Process: Comprueba que x e y estén entre -200 y 190.
    Output: Booleano True si está dentro, False si no.
    """
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """
    Mueve la serpiente y la comida un segmento.
    Input: Ninguno explícito (usa variables globales).
    Process:
      - Calcula la nueva posición de la cabeza.
      - Valida colisiones.
      - Actualiza la posición de la comida de forma aleatoria.
      - Dibuja los elementos en pantalla.
    Output: Renderizado en pantalla actualizado.
    """
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
    else:
        snake.pop(0)

    # Movimiento aleatorio de la comida (1 paso a la vez)
    food.x += choice([-10, 0, 10])
    food.y += choice([-10, 0, 10])

    # Mantener la comida dentro de los límites de la ventana
    if food.x < -200:
        food.x = -200
    elif food.x > 190:
        food.x = 190

    if food.y < -200:
        food.y = -200
    elif food.y > 190:
        food.y = 190

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
done()
