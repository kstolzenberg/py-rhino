# Cesaro Torn Line Square
from Tkinter import *
import turtle

window = turtle.Screen()
window.bgcolor('black')
window.title('Cesaro Torn Line')

draw = turtle.Turtle()
draw.color('green')
draw.pensize(2)
draw.speed('fastest')

def cesaro(order, size):
    ''' Makes the turtle draw a Cesaro Koch curve of specified order and size
    '''
    if order == 0:
        draw.forward(size)
    else:
        cesaro(order - 1, size / 3)
        draw.right(85)
        cesaro(order - 1, size / 3)
        draw.left(170)
        cesaro(order - 1, size / 3)
        draw.right(85)
        cesaro(order - 1, size / 3)

for i in range(4):     # loop to draw square form
    cesaro(3, 400)
    draw.right(90)

#turtle.mainloop()
ts = turtle.getscreen()
ts.getcanvas().postscript(file="csquare.eps")

