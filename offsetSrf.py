import rhinoscriptsyntax as rs

srfs = rs.GetObjects("pick srfs")

# need a structure of a list of arrays of 4 srfs
fourSrfs = rs.ExplodePolysurfaces(srfs,True)
thickSrfs = []

#for srf in singleSrfs:
#    thick = rs.OffsetSurface(srf,-1,None,False, True)
#    rs.DeleteObject(srf)
#    thickSrfs.append(thick) 

# this boolean fails because its try things that don't touch - you need a data structure for each quad
#solids = rs.BooleanUnion(thickSrfs,True)

print solids
print "done"