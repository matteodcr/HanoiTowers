turtle = None

def set_turtle(t):
    global turtle
    turtle = t

def tourner_droite():
    turtle.right(90)

def tourner_gauche():
    turtle.left(90)

def rect(x, y, width, height, color = 'black', fill_color: str = None):
    assert turtle != None, 'set_turtle was not called'

    turtle.goto(x - 255, y - 100)

    turtle.pencolor(color)
    if (fill_color is not None):
        turtle.fillcolor(fill_color)
        turtle.begin_fill()
    else:
        turtle.down()
    
    for _ in range(0,2):
        turtle.forward(width)
        tourner_gauche()
        turtle.forward(height)
        tourner_gauche()
    
    turtle.pencolor('black')
    if (fill_color is not None):
        turtle.end_fill()
        turtle.fillcolor('black')
    else:
        turtle.up()
