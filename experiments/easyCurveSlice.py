# this is so easy!!!

import rhinoscriptsyntax as rs

curve_id = rs.GetObject("pick a crv", 4) # get curve
points = rs.DivideCurve(curve_id, 10) # returns a list of points

print points[1]

for i in points:
    rs.AddSphere(i, 1) # add a sphere at each point in list with radius =1