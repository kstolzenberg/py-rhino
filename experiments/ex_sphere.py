# modified from RhinoPythonPrimer Rev3
import math
import rhinoscriptsyntax as rs

pi = math.pi
dblTwistAngle = 0.0

rs.EnableRedraw(False)
for z in rs.frange(0.0, 5.0, 0.5):
    dblTwistAngle = dblTwistAngle + (pi/30)
    
    for a in rs.frange(0.0, 2*pi, (pi/15)):
        x = 5 * math.sin(a + dblTwistAngle)
        y = 5 * math.cos(a + dblTwistAngle)
        rs.AddSphere([x,y,z], 0.5)
      
rs.EnableRedraw(True)
