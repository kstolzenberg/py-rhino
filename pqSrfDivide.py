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
for crv in allCrvZip:
    allCrvsU.append(rs.ExtractIsoCurve(newSrf, crv, 0))

for crv in allCrvZip:
    allCrvsV.append(rs.ExtractIsoCurve(newSrf, crv, 1))

    
u_curves = []
v_curves = []

# cleanup curves
for crv in allCrvsU:
    if crv:
        u_curves.append(crv[0])
for crv in allCrvsV:
    if crv:
        v_curves.append(crv[0])


# make a list of adjacent curves pairs in each direction
for i in range(len(v_curves)-1):
    adjCrvsV.append((v_curves[i],v_curves[i+1]))
    
for i in range(len(u_curves)-1):
    adjCrvsU.append((u_curves[i],u_curves[i+1]))
                 
                    
quads = []
for row in adjCrvsU:
    for column in adjCrvsV:
        a = rs.CurveCurveIntersection(row[0],column[0])
        b = rs.CurveCurveIntersection(row[0],column[1])
        c = rs.CurveCurveIntersection(row[1],column[1])
        d = rs.CurveCurveIntersection(row[1],column[0])
        
        if all([a, b, c, d]):
            quads.append((a[0][1], b[0][1], c[0][1], d[0][1]))

for pt in quads[0]:
    newPt = rs.AddPoint(pt)
    rs.SelectObject(newPt)

for quad in quads:
    rs.AddSrfPt(quad)

