# from RhinoRythonPrimerRev3

import rhinoscriptsyntax as rs

def flatWorm():
    curveObject = rs.GetObject("pick a backbone curve", 4, True, False)
    samples = rs.GetInteger("# of crosssections", 100, 5)
    bend_radius = rs.GetReal("bend radius", 0.5, 0.001) # r1
    perp_radius = rs.GetReal("ribbon plan radius", 2.0, 0.001) #r2
    crvDom = rs.CurveDomain(curveObject) # domain != length // why do we use domains? == "The domain is the set of all possible input values to the function that defines the curve or surface."

    crossSections = [] # empty array to store sections
    t_step = (crvDom[1] - crvDom[0]) / samples # this is starting to be a pattern!
    t = crvDom[0] # start pt for loop at the start of the line

    for t in rs.frange(crvDom[0], crvDom[1], t_step): # loop thru entire domain w/ floats
        crvCurvature = rs.CurveCurvature(curveObject, t) # evaluate curve with a circle - gives 3d normals & gives radius info
        crossSecPlane = None
        if not crvCurvature:
            crvPoint = rs.EvaluateCurve(curveObject, t)
            crvTan = rs.CurveTangent(curveObject, t) # get tangent vector
            crvPerp = (0,0,1)
            crvNorm = rs.VectorCrossProduct(crvTan, crvPerp)# = product of 2 vectors
            crossSecPlane = rs.PlaneFromFrame(crvPoint, crvPerp, crvNorm)
        else:
            crvPoint = crvCurvature[0]
            crvTan = crvCurvature[1]
            crvPerp = rs.VectorUnitize(crvCurvature[4])
            crvNorm = rs.VectorCrossProduct(crvTan, crvPerp)# look up
            crossSecPlane = rs.PlaneFromFrame(crvPoint, crvPerp, crvNorm)
        if crossSecPlane:
            csec = rs.AddEllipse(crossSecPlane, bend_radius, perp_radius) # draw ellipse at tan/normal to point along curve with radii
            crossSections.append(csec) # add ellipses to an array
        t += t_step # step through domain

    rs.AddLoftSrf(crossSections) # loft list of curves
    rs.DeleteObjects(crossSections) # delete original list of curves as cleanup

flatWorm()