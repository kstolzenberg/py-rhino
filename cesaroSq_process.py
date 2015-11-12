# testing turtlebot equivalency...rotate cPlane/"pen head"
import rhinoscriptsyntax as rs

plane = rs.ViewCPlane()
rs.AddRectangle(plane,24,48)
plane = rs.RotatePlane(plane, -80,[0,0,1] ) # note negative goes to the right
rs.AddRectangle(plane,24,48)
