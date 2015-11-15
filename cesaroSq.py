# Adapted from turtle script NYU CS Course here http://cs.nyu.edu/courses/spring13/CSCI-UA.0002-008/notes/code/cesaro-square.py
import rhinoscriptsyntax as rs 
 
plane = rs.ViewCPlane()
# lets try this with rectangles or else in hybrid gh model because there is no "LineSDL" supported in python...there is in gh tho
# the start position isn't incrementing.. the plane position needs to updating

def cesaro(order, size):  
    global plane
    if order == 0:
       rs.AddRectangle(plane,2, size) 
       
    else:
        cesaro(order - 1, size / 3)
        #draw.right(80) these are degrees
        plane = rs.RotatePlane(plane, 80, [0,0,1])
        cesaro(order - 1, size / 3)
        plane = rs.RotatePlane(plane, -160, [0,0,1])
        cesaro(order - 1, size / 3)
        plane = rs.RotatePlane(plane, 80, [0,0,1])
        cesaro(order - 1, size / 3)

for i in range(4):
    cesaro(2, 300)
    plane = rs.RotatePlane(plane, 90, [0,0,1])
    
print "done"
