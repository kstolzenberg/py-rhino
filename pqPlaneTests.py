# test for methods for the PQ mesh

import rhinoscriptsyntax as rs
import pprint # print pretty for lists

# corners = rs.GetObjects("select corners")
# rs.AddSrfPt(corners)
# THIS BASE CASE WORKS! ORDER MATTERS - YOU JUST HAVE TO GO CLOCKWISE OR COUNTER, NO OPPOSITES

## need to loop and serialize this for all curves and all points, not just two points!!!
#crvs = rs.GetObjects("pick 2 curves to intersect")
#
## note this spits back a list of info, first = type of intersect then points
#intersectResult = rs.CurveCurveIntersection(crvs[0], crvs[1])
#pprint.pprint intersectResult
#
#if intersectResult[0][0] == 1:
#    intPt = rs.AddPoint(intersectResult[0][1])
#else:
#    print "not intersecting"

allpt = rs.GetObjects("get pts")
pprint.pprint(allpt)

points = [allpt[1], allpt[2], allpt[3], allpt[4]]
rs.AddSrfPt(points)
