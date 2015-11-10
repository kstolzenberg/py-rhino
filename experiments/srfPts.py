# common pattern of patterning a surface!
import rhinoscriptsyntax as rs

def ptsOnSrf ():
    surfaceId = rs.GetObject("pick surface", 8, True, True)
    uVal = rs.GetInteger("pick u/row count",4, 1, 20)
    vVal = rs.GetInteger("pick v/col count",4, 1, 20)
    uDomain = rs.SurfaceDomain(surfaceId, 0)
    vDomain = rs.SurfaceDomain(surfaceId, 1)
    uStep = (uDomain[1] - uDomain[0])/ uVal
    vStep = (vDomain[1] - vDomain[0])/ vVal
    count = 0
    
    for i in rs.frange(uDomain[0], uDomain[1], uStep):
        for j in rs.frange(vDomain[0], vDomain[1], vStep):
            point = rs.EvaluateSurface(surfaceId, i, j)
            newPt = rs.AddPoint(point)
            count += 1
            rs.AddText(count,newPt, .25)
    
ptsOnSrf()