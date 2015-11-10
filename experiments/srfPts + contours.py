# creates interpolated curve from a surface - not sure where this would used
# note that at somepoint, this is as much work as the gui??? careful on user input

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
    allPts = []
    
    for i in rs.frange(uDomain[0], uDomain[1], uStep):
        for j in rs.frange(vDomain[0], vDomain[1], vStep):
            point = rs.EvaluateSurface(surfaceId, i, j)
            newPt = rs.AddPoint(point)
            allPts.append(newPt)
            
    rs.AddInterpCrvOnSrf(surfaceId, allPts)
    rs.DeleteObjects(allPts)

def contour (crvOffset):
    # get geometry
    surfaceId = rs.GetObject("pick surface to contour", 0, True, True)
    startPt = rs.GetPoint("base point of contours")
    endPt = rs.GetPoint("end point of contours")
    count = 0
    reference = []
    target = []

    # make contours & store in newCrvs
    newCrvs = rs.AddSrfContourCrvs(surfaceId, (startPt, endPt), crvOffset) # output is a list of GUIDs. can't access raw points

    # divide the target surface
    printBed = rs.GetObject("pick surface for layout", 8, True, True)
    intCount = len(newCrvs)
    uDomain = rs.SurfaceDomain(printBed, 0)
    vDomain = rs.SurfaceDomain(printBed, 1)
    uStep = (uDomain[1] - uDomain[0]) / intCount

    for u in rs.frange(uDomain[0], uDomain[1], uStep):
        layout = rs.SurfaceFrame(printBed, [u,1])
        target1 = layout[0] # set target to point inside of object - note this is a single point
        target2 = rs.PointAdd(target1,(0,10,0)) # this could be more parametric
        target.extend([target1, target2])
    #print target

    # add text, reference and orient!
    # for orient, we need a list 3 points to reference and 3 points to target!
    # maybe reference should be curve origin crvPl[0] and midpoint? or else polyline verticies -- need to convert curve to polyline first? 
    for crv in newCrvs:
        count += 1 # for label
        crvPl = rs.CurvePlane(crv) # plane for text
        rs.AddText(count, crvPl, 0.25) # should you label on the ground?
        #crvPl = rs.PointAdd(crvPl[0], (0,0,-1)) # if you wanted to offset text
        ref1 = rs.CurveMidPoint(crv) 
        ref2 = crvPl[0]
        reference.extend([ref1, ref2])
    #print reference
        
        # this is closer but still doesn't work!!
        # we need reference = ((),()) & target = ((),())   
        #for i in range(0, intCount - 1):
            #rs.OrientObject(crv, reference[i], target[i])

contour(2)
#ptsOnSrf()

# This issue is the array lengths - should be 11 in target and reference!!!
# make sure its orient 3pt!! seems to work better than other