from turtle import *


def tourner_droite():
    right(90)

def tourner_gauche():
    left(90)

def rect(x, y, width, height, color = 'black', fill_color: str = None):
    goto(x - 300, y + 180)

    pencolor(color)
    if (fill_color is not None):
        fillcolor(fill_color)
        begin_fill()
    else:
        down()
    
    for i in range(0,2):
        forward(width)
        tourner_gauche()
        forward(height)
        tourner_gauche()
    
    pencolor('black')
    if (fill_color is not None):
        end_fill()
        fillcolor('black')
    else:
        up()
