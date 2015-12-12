import rhinoscriptsyntax as rs 
 
plane = rs.ViewCPlane()

def cesaro(order, size):  
    global plane
    
    if order == 0:
       rs.AddRectangle(plane,2, size) # this plane needs to be dynamically moving!
    else:
        for angle in [80,-160, 80, 0]:           
            cesaro(order-1, size/3) # this isn't recursively changing??? and it crashes when pulled out as sep var
            print size # this should be getting smaller no?
            plane = rs.RotatePlane(plane, angle, [0,0,1])

cesaro(3, 300)    
print "done"
