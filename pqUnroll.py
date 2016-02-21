import rhinoscriptsyntax as rs

srfToUnroll = rs.GetObjects("select srfs")


for srf in srfToUnroll:
    #flatSrf = rs.UnrollSurface(srf, False)
    #rs.AddText()
    #space = pt.X + 5
    #rs.MoveObject(flatSrf, (5+i,0,0))    
    
    cutCrvs = rs.DuplicateEdgeCurves(srf)
    
#print cutCrvs
