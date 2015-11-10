# build a model of planar quads from a surface

import rhinoscriptsyntax as rs

newSrf = rs.GetObject("pick ur start")

# get domain to split
Udom = rs.SurfaceDomain(newSrf, 0)
Vdom = rs.SurfaceDomain(newSrf, 1)
dom = (Udom[1], Vdom[1])
# print dom

divisor = 10
uDomAll = []
vDomAll = []
allCrvs = []


# divide domain by an increment
def divideDomain(domainTuple, divisor, domList): 
    
    for i in range(divisor):
        step = (domainTuple[1]- domainTuple[0]) / divisor 
        i *= step
        domList.append(i)
   
    domList.append(domainTuple[1]) # add last curve!

divideDomain(Udom, divisor, uDomAll)
divideDomain(Vdom, divisor, vDomAll)


# create UV tuples from U & V divided domain
allCrvZip = zip(uDomAll, vDomAll)


# extract isocurves per domain increment
for i in range(len(allCrvZip)):
    allCrvs.append(rs.ExtractIsoCurve(newSrf, allCrvZip[i], 2))


# group all extracted lines
edges = rs.DuplicateEdgeCurves(newSrf, False)
#allCrvs.append(edges)
wireGroup = rs.AddGroup()
for i in allCrvs:
    rs.AddObjectsToGroup(i, wireGroup)

# get all isocurve intersections as points and draw planar surfaces between these points
# rs.CurveCurveIntersection(allCrv[0],allCrv[1]) # see other method for point from int
# note allCrvs is a list of GUIDs representing the isocurves. need to order or figure out corner relationships