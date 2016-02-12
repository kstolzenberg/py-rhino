# Adapted from turtle script NYU CS Course here http://cs.nyu.edu/courses/spring13/CSCI-UA.0002-008/notes/code/cesaro-square.py
import rhinoscriptsyntax as rs 
import math

plane = rs.ViewCPlane()

class Turtle():
    def __init__(self):
        #self.position = (0,0,0)
        plane = rs.ViewCPlane()
        #print plane
        self.position = plane[0]
        #plane needs to relate back to position
        

    def forward(self, length):
        start = self.position
        end = (start[0]+length, 0,0)
        #rs.AddLine(start, end)
        rs.Line()
        self.position = end

# is there any way to do this without doing the trig? depends on which way you go!
# x1 = x0 + L*cos(degrees)
# y1 = y0 + L*sin(degrees)

def cesaro(order, size):  
    global plane
    if order == 0:
      turtle.forward(size)
    else:
        cesaro(order - 1, size / 3)
        #draw.right(80) these are degrees
        turtle.plane = rs.RotatePlane(plane, 80, [0,0,1])
        cesaro(order - 1, size / 3)
        turtle.plane = rs.RotatePlane(plane, -160, [0,0,1])
        cesaro(order - 1, size / 3)
        turtle.plane = rs.RotatePlane(plane, 80, [0,0,1])
        cesaro(order - 1, size / 3)

turtle = Turtle()

for i in range(4):
    cesaro(1, 300)
    turtle.plane = rs.RotatePlane(plane, 90, [0,0,1])

