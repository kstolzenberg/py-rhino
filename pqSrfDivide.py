# build a model of planar quads from a surface
# eventually roll this into a function that can be run separately for the U and V direction...very parallel!

import rhinoscriptsyntax as rs
import pprint

newSrf = rs.GetObject("pick ur start")

# get domain to split
Udom = rs.SurfaceDomain(newSrf, 0)
Vdom = rs.SurfaceDomain(newSrf, 1)
dom = (Udom[1], Vdom[1])

divisor = 10
uDomAll = []
vDomAll = []
#allCrvs = []
allCrvsU = []
allCrvsV = []
adjCrvsV = []
adjCrvsU = []


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

# extract isocurves per domain increment, increment and draw point?
for i in range(len(allCrvZip)):
    allCrvsU.append(rs.ExtractIsoCurve(newSrf, allCrvZip[i], 0))

for i in range(len(allCrvZip)):
    allCrvsV.append(rs.ExtractIsoCurve(newSrf, allCrvZip[i], 1))

# make a list of adjacent curves pairs in each direction
for i in range(1, len(allCrvsV)-1):
    adjCrvsV.append([allCrvsV[i],allCrvsV[i+1]])
    
for i in range(1, len(allCrvsU)-1):
    adjCrvsU.append([allCrvsU[i],allCrvsU[i+1]])
    
#rs.SelectObjects(adjCrvsV[0])
        
# create a new structure checking intersections between curves and adding points to a new data structue
# but these are pairs not individual curves..may have to reach further down!
# if they don't intersect...it will just return 'None'
for i in adjCrvsU:
    for j in adjCrvsV:
        try:
            rs.CurveCurveIntersection(i,j)
        except():
            pass         



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