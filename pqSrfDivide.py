# build a model of planar quads from a surface
# eventually roll this into a function that can be run separately for the U and V direction...very parallel!

import rhinoscriptsyntax as rs
import pprint

newSrf = rs.GetObject("pick ur start")

# get domain to split
Udom = rs.SurfaceDomain(newSrf, 0)
Vdom = rs.SurfaceDomain(newSrf, 1)
dom = (Udom[1], Vdom[1])

divisor = 20 # keep this even duh!
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
    
#print adjCrvsU[0][0]

for i in range(len(adjCrvsU)):
    for j in range(len(adjCrvsV)):
        print "1:",(adjCrvsU[i][0],adjCrvsV[j][0])
        print "2:" , (adjCrvsU[i][0],adjCrvsV[j][1])
        print "3:", (adjCrvsU[i][1],adjCrvsV[j][0])
        print "4:", (adjCrvsU[i][1],adjCrvsV[j][1])
#        a = rs.CurveCurveIntersection(adjCrvsU[i][0],adjCrvsV[j][0])
#        b = rs.CurveCurveIntersection(adjCrvsU[i][0],adjCrvsV[j][1])
#        c = rs.CurveCurveIntersection(adjCrvsU[i][1],adjCrvsV[j][1])
#        d = rs.CurveCurveIntersection(adjCrvsU[i][1],adjCrvsV[j][0])
#        
#        if a and b != None:
#            print a
#            print b
#        
#        try:
#            print rs.CurveCurveIntersection(adjCrvsU[i][0],adjCrvsV[j][0])
#            print rs.CurveCurveIntersection(adjCrvsU[i][0],adjCrvsV[j][1])
#            print rs.CurveCurveIntersection(adjCrvsU[i][1],adjCrvsV[j][0])
#            print rs.CurveCurveIntersection(adjCrvsU[i][1],adjCrvsV[j][1])
#        except:
#            pass    


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