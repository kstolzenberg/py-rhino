# test for methods for the PQ mesh

import rhinoscriptsyntax as rs
import pprint # print pretty for lists

#corners = rs.GetObjects("select corners")
#rs.AddSrfPt(corners)
# THIS WORKS!!! :)
# DOES ORDER MATTER? YES OTHERWISE IT WILL TWIST. YOU JUST HAVE TO GO CLOCKWISE OR COUNTERCLOSCKWISE. NO CORNERS.
# WE NEED A WAY TO ORDER THE CORNERS SO THAT THINGS ARE NEXT TO EACH OTHER!

# need to loop and serialize this for all points, not just two points!!!
crvs = rs.GetObjects("pick 2 curves to intersect")

# note this spits back a list of info, first = type of intersect then points
intersectResult = rs.CurveCurveIntersection(crvs[0], crvs[1])
pprint.pprint intersectResult

if intersectResult[0][0] == 1:
    intPt = rs.AddPoint(intersectResult[0][1])
else:
    print "not intersecting"
