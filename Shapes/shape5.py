import turtle
t = turtle.Turtle()
t.getscreen().bgcolor("black")
t.penup()
t.goto(-200, 100)
t.pendown()
t.color("yellow")
t.speed(25)
def star(turtle, size):
    if size<=10:
        return
    else:
        turtle.begin_fill()
        for i in range (5):
            turtle.pensize(2)
            turtle.forward(size)
            star(turtle, size/3)
            turtle.left(216)
            turtle.end_fill()
star(t, 360)
turtle.done()
