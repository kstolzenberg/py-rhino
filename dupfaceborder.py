
import rhinoscriptsyntax as rs

srfToUnroll = rs.GetObjects("select srfs")


for srf in srfToUnroll:
    cutCrvs = rs.DuplicateEdgeCurves(srf)
    
print cutCrvs
