import rhinoscriptsyntax as rs

polySrfs = rs.GetObjects("pick polysrfs")

AllSrfs = [] # this is a list of lists of each polysurface shape
thickSrfs = []

# need a structure of a gloabl list of arrays of 4 srfs
# the answer is always needz more data structure

for obj in polySrfs:
    AllSrfs.append(rs.ExplodePolysurfaces(obj,True))

for shape in AllSrfs:
    thick_shapes = []
    for srf in shape:
        thick = rs.OffsetSurface(srf,-.5,None,False,True)
        rs.DeleteObject(srf)
        thick_shapes.append(thick)
    
    print rs.BooleanUnion(thick_shapes)

# need to add merge face support - something in Rhino Common? 
# Rhino.Geometry.Brep.MergeCoplanarFaces

print "done"