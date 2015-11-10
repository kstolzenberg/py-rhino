# from RhinoRythonPrimerRev3
# need to define another way to draw arcs bc OOTB = plane/rad or 3pt. - using vector math

import rhinoscriptsyntax as rs

def addArcDiv(ptStart, ptEnd, vecDir):
    vecBase = rs.PointSubtract(ptEnd, ptStart)
    # error handling
    if rs.VectorLength(vecBase) == 0.0: return
    if rs.IsVectorParallelTo(vecBase, vecDir): return
    
    vecBase = rs.VectorUnitize(vecBase) # normalize vector == force magnitude to 1 to just compare direction
    vecDir = rs.VectorUnitize(vecDir)
    vecBisector = rs.VectorAdd(vecDir, vecBase)
    vecBisector = rs.VectorUnitize(vecBisector)
    
    dotProd = rs.VectorDotProduct(vecBisector, vecDir)
    midLength = (0.5 * rs.Distance(ptStart, ptEnd)) / dotProd
    
    vecBisector = rs.VectorScale(vecBisector, midLength)
    return rs.AddArc3Pt(ptStart, rs.PointAdd(pt.Start, vecBisector), ptEnd)

