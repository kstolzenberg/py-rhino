# build a model of planar quads from a surface

import rhinoscriptsyntax as rs
import pprint

newSrf = rs.GetObject("pick ur start")

# get domain to split
Udom = rs.SurfaceDomain(newSrf, 0)
Vdom = rs.SurfaceDomain(newSrf, 1)
dom = (Udom[1], Vdom[1])
# print dom

divisor = 20
uDomAll = []
vDomAll = []
allCrvs = []
allCrvsU = []
allCrvsV = []


# divide domain by an increment
def divideDomain(domainTuple, divisor, domList): 
    
    for i in range(divisor):
        step = (domainTuple[1]- domainTuple[0]) / divisor 
        i *= step
        domList.append(i)
   
    domList.append(domainTuple[1]) # add last curve!

divideDomain(Udom, divisor, uDomAll)
divideDomain(Vdom, divisor, vDomAll)

# create UV tuples from U & V divided domain - note this is ordered!
allCrvZip = zip(uDomAll, vDomAll)
# print allCrvZip # note this is ordered from smallest to largest

# this is a point on the untrimmed surace - off our surface? :<
#test = rs.EvaluateSurface(newSrf, allCrvZip[1][0], allCrvZip[1][1])
#newpt = rs.AddPoint(test)
#rs.SelectObject(newpt)

# extract isocurves per domain increment, increment and draw point?
# maybe better to extract all in one direction, then all in the other, then can iterate over? these are now in selectable order.
# for this assignment would be helpful to go from u/v curves lists to panels as a  module.
for i in range(len(allCrvZip)):
    #allCrvs.append(rs.ExtractIsoCurve(newSrf, allCrvZip[i], 2))
    allCrvsU.append(rs.ExtractIsoCurve(newSrf, allCrvZip[i], 0))

# it doesn't look this output is ordered by adjacency...they are opposite! is possible to sort by uv curves?   
#rs.SelectObject(allCrvs[2][0])
#rs.SelectObject(allCrvs[2][1])

for i in range(len(allCrvZip)):
    allCrvsV.append(rs.ExtractIsoCurve(newSrf, allCrvZip[i], 1))

# why does the isocurve list have an empty tuple at the end and at the beginging? those aren't present in the uv pairs
# note the origins are opposite? what if you reverse the list.....reversing doesn't help... how to find the similar ones?
# allCrvsV[::-1]
print len(allCrvsU)
rs.SelectObject(allCrvsU[1])
rs.SelectObject(allCrvsU[2])
rs.SelectObject(allCrvsV[10])
rs.SelectObject(allCrvsV[9])


#    intersectResult = rs.CurveCurveIntersection(crvs[i], crvs[i+1])
#    pprint.pprint intersectResult
#    
#    if intersectResult[0][0] == 1:
#        intPt = rs.AddPoint(intersectResult[0][1])
#    else:
#        print "not intersecting"


# group all extracted lines
#edges = rs.DuplicateEdgeCurves(newSrf, False)
#allCrvs.append(edges)
#wireGroup = rs.AddGroup()
#for i in allCrvs:
#    rs.AddObjectsToGroup(i, wireGroup)

# get all isocurve intersections as points and draw planar surfaces between these points
# rs.CurveCurveIntersection(allCrv[0],allCrv[1]) # see other method for point from int
# note allCrvs is a list of GUIDs representing the isocurves. need to order or figure out corner relationships