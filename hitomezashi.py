from turtle import Screen, Turtle
import numpy as np

GRID_HEIGHT = 22
GRID_WIDTH = 22
GRID_SIZE = GRID_HEIGHT * GRID_WIDTH
PROBABILITY = 0.55

# Generate random binary sequence
def gen(size):
    vec = np.random.rand(size) > PROBABILITY
    return vec

# Make drawing
def draw():
    horizontal = gen(GRID_HEIGHT)
    vertical = gen(GRID_WIDTH)

    step = 22
    screen = Screen()
    screen.tracer(0)
    turtle = Turtle()
    turtle.width(1.5)
    turtle.color('white', '#4B0082')
    turtle.hideturtle()
    turtle.speed(0)
    
    # Draw contour
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(-GRID_SIZE / 2, -GRID_SIZE / 2)
    turtle.pendown()

    for i in range(GRID_WIDTH):
        turtle.forward(step)

    turtle.left(90)

    for i in range(GRID_HEIGHT):
        turtle.forward(step)

    turtle.left(90)

    for i in range(GRID_WIDTH):
        turtle.forward(step)

    turtle.left(90)

    for i in range(GRID_HEIGHT):
        turtle.forward(step)
    turtle.end_fill()

    turtle.penup()
    turtle.left(90)
    turtle.goto(-GRID_SIZE / 2, -GRID_SIZE / 2)
    turtle.pendown()

    # Draw horizontal lines
    h = 1
    for bool in horizontal:
        if bool:
            for i in range(GRID_HEIGHT):
                if i % 2 == 1:
                    turtle.penup()
                    turtle.forward(step)
                    turtle.pendown()
                else:
                    turtle.forward(step)
        else:
            for i in range(GRID_WIDTH):
                if i % 2 == 0:
                    turtle.penup()
                    turtle.forward(step)
                    turtle.pendown()
                else:
                    turtle.forward(step)
        turtle.penup()
        turtle.goto(-GRID_SIZE / 2, -GRID_SIZE / 2 + step * h)
        turtle.pendown()
        h = h+1
    
    turtle.penup()
    turtle.goto(-GRID_SIZE / 2, GRID_SIZE / 2)
    turtle.right(90)
    turtle.pendown()

    # Draw vertical lines
    h = 1
    for bool in vertical:
        if bool:
            for i in range(GRID_WIDTH):
                if i % 2 == 1:
                    turtle.penup()
                    turtle.forward(step)
                    turtle.pendown()
                else:
                    turtle.forward(step)
        else:
            for i in range(GRID_WIDTH):
                if i % 2 == 0:
                    turtle.penup()
                    turtle.forward(step)
                    turtle.pendown()
                else:
                    turtle.forward(step)
        turtle.penup()
        turtle.goto(-GRID_SIZE / 2 + step * h, GRID_SIZE / 2)
        turtle.pendown()
        h = h+1

    screen.update()
    screen.mainloop() 
    screen.exitonclick()

draw()