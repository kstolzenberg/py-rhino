import rhinoscriptsyntax as rs

srfToUnroll = rs.GetObjects("select srfs")


for srf in srfToUnroll:
    cutCrvs = rs.DuplicateEdgeCurves(srf)
    rs.UnrollSurface(srf, False, cutCrvs)
    
print cutCrvs
