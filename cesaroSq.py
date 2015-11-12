# Adapted from turtle script NYU CS Course here http://cs.nyu.edu/courses/spring13/CSCI-UA.0002-008/notes/code/cesaro-square.py
import rhinoscriptsyntax as rs  

plane = rs.ViewCPlane()

#plane = rs.ViewCPlane()
#rs.AddRectangle(plane,24,48)
#plane = rs.RotatePlane(plane, -80,[0,0,1] ) # note negative goes to the right
#rs.AddRectangle(plane,24,48)

def cesaro(order, size):  
    if order == 0:
        end = (size, 0, 0)
        start = (0,0,0)
        rs.AddLine(start, end) # this might be a problem because you really just want it in terms of length & starting plane!
    else:
        cesaro(order - 1, size / 3)
        #draw.right(80) these are degrees
        rs.RotatePlane(plane, 80, [0,0,1])
        cesaro(order - 1, size / 3)
        rs.RotatePlane(plane, -160, [0,0,1])
        cesaro(order - 1, size / 3)
        rs.RotatePlane(plane, 80, [0,0,1])
        cesaro(order - 1, size / 3)
        

for i in range(4):
    cesaro(2, 300)
    rs.RotatePlane(plane, 90, [0,0,1])
    
print "done"
