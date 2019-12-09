turtle = None


def set_turtle(t):
    global turtle
    turtle = t


def rect(x, y, width, height, color = 'black', fill_color: str = None):
    assert turtle != None, 'set_turtle was not called'

    x -= 255
    y -= 100

    turtle.goto(x, y)

    turtle.pencolor(color)
    if (fill_color is not None):
        turtle.fillcolor(fill_color)
        turtle.begin_fill()
    else:
        turtle.down()
    
    turtle.goto(x + width, y)
    turtle.goto(x + width, y + height)
    turtle.goto(x, y + height)
    turtle.goto(x, y)
    
    turtle.pencolor('black')
    if (fill_color is not None):
        turtle.end_fill()
        turtle.fillcolor('black')
    else:
        turtle.up()
