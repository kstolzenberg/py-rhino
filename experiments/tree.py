# modify classic recursive tree example for Rhino

import rhinoscriptsyntax as rs
import math
import random

# how to make this actually 3d?
def drawTree(x1, y1, z1, angle, depth):
    points = []
    if depth:
        z2 = z1 + int(math.cos(math.radians(angle)) * depth * 5.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 5.0)
        x2 = 0 # tan is not the ticket
        start = rs.AddPoint(x1, y1, z1)
        points.append(start)
        end = rs.AddPoint(x2, y2, z2)
        points.append(end)
        #rs.AddLine(start, end)
        #rs.AddSphere(end, 1)
        dir = (random.randint(0,20), random.randint(0,20), random.randint(0,20))
        rs.AddArcPtTanPt(start, dir, end)
        drawTree(x2, y2, z2, angle - random.randint(10, 60), depth -1)
        drawTree(x2, y2, z2, angle + random.randint(10, 40), depth -1)
        rs.DeleteObjects(points)

drawTree(0, 0, 0, 0, 5)