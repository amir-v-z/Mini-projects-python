from turtle import *

colors=["red","green","yellow","white","blue","orange"]

bgcolor("black")
speed(0)

for i in range(300):
    pencolor(colors[i%len(colors)])
    forward(i)
    left(59)

done()