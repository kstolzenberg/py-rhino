import rhinoscriptsyntax as rs

polySrfs = rs.GetObjects("pick polysrfs")

fourSrfs = [] # this is a list of lists of each polysurface shape
allSrfs = [] # not sure you need this the other one is already an arrray!
thickSrfs = []

# need a structure of a gloabl list of arrays of 4 srfs
# the answer is always needz more data structure

for obj in polySrfs:
    fourSrfs.append(rs.ExplodePolysurfaces(obj,True))

print fourSrfs

for srf in fourSrfs[0]:
    thick = rs.OffsetSurface(srf,-1,None,False,True)
    rs.DeleteObject(srf)
    thickSrfs.append(thick)

solid = rs.BooleanUnion(thickSrfs,True)

# need to add merge face support - something in Rhino Common? 
# Rhino.Geometry.Brep.MergeCoplanarFaces

#for srf in singleSrfs:
#    thick = rs.OffsetSurface(srf,-1,None,False, True)
#    rs.DeleteObject(srf)
#    thickSrfs.append(thick) 

# this boolean fails because its try things that don't touch - you need a data structure for each quad
#solids = rs.BooleanUnion(thickSrfs,True)

print "done"