# build a model of planar quads from a catalog of surfaces

import rhinoscriptsyntax as rs

newSrf = rs.GetObject("pick ur start")

#note this is only extracting the first isocurves, need to get a list going to loop over 
Udom = rs.SurfaceDomain(newSrf, 0)
Vdom = rs.SurfaceDomain(newSrf, 1)
dom = (Udom[1], Vdom[1])
# print dom

divisor = 10
uDomAll = []
vDomAll = []

# need divide domain function to iterate curves over - should this be evaluate surface or divide domain?

def divideDomain(domainTuple, divisor, domList): 
    
    for i in range(divisor):
        step = (domainTuple[1]- domainTuple[0]) / divisor 
        i *= step
        domList.append(i)
   
    domList.append(domainTuple[1]) # add last curve!

divideDomain(Udom, divisor, uDomAll)
divideDomain(Vdom, divisor, vDomAll)

# you may not want them all together - you may prefer as zip list!
# allCrv = uDomAll + vDomAll
# print "all the curves %r" % allCrv

# zipping correct U V tuples
allCrvZip = zip(uDomAll, vDomAll)

# note this give only last isocurves in u and v! we now need to loop over the fat list?
# allCrvU = rs.ExtractIsoCurve(newSrf, dom, 2)

allCrvs = []

for i in range(len(allCrvZip)):
    allCrvs.append(rs.ExtractIsoCurve(newSrf, allCrvZip[i], 2))

# group all these lines...not iterating properly - try singular
edges = rs.DuplicateEdgeCurves(newSrf, False)
#allCrvs.append(edges)

wireGroup = rs.AddGroup()
for i in allCrvs:
    rs.AddObjectsToGroup(i, wireGroup)

# draw shape
# get intersections as points and draw iso curves through? would want the previous lists then without edge?

# rs.CurveCurveIntersection(allCrv[0],allCrv[1]) # note this doesn't split! but neither does wireframe!
# evaluateCurve will a point at a number....can this be the intersection?
# note allCrvs is a list of GUIDs representing the isocurves