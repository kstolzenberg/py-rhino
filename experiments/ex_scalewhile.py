# modified from RhinoPythonPrimer Rev3
import rhinoscriptsyntax as rs

def scalecurve():
    curve_id = rs.GetObject("pick curve", 4)
    
    # provide breakout bc idk
    if curve_id is None:
        return
    
    length = rs.CurveLength(curve_id)
    print "current length: %g " % length
    length_max = rs.GetReal("max length? ", .5* length, .1 * length, 10 * length) # you can set ranges!
    
    if length_max is None:
        return
    
    while length < length_max:
        curve_id = rs.ScaleObject(curve_id, (0,0,0), (1.5, 1.5, 1.5), True)
        length = rs.CurveLength(curve_id)
        print "new curve length: %g" % rs.CurveLength(curve_id)
   
scalecurve()