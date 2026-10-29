
"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
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
# Allowed colors; red is excluded on purpose.
COLORS = ['blue', 'green', 'orange', 'purple', 'brown']
# Pick two different colors once per game.
snake_color, food_color = sample(COLORS, 2)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():
    """Mueve la comida un paso de 10 al azar sin salirse de la ventana."""
    step = choice([vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)])
    new_food = food.copy()
    new_food.move(step)

    if inside(new_food):
        food.move(step)
def move():
    """Move snake forward one segment."""
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
    move_food()
    move_food()

    clear()
    for body in snake:
        ...
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
