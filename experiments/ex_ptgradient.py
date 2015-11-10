# modified from RhinoPythonPrimer Rev3
import rhinoscriptsyntax as rs

def main():
    curve_id = rs.GetObject("pick curve to sample", 4, True, True)
    rs.EnableRedraw(False)
    t = 0
    while t <= 1.0:
        addPoint(curve_id, t) # add point to selected curve
        t += 0.002 # add points at this increment
    rs.EnableRedraw(True)
    
def addPoint(curve_id, parameter):
    domain = rs.CurveDomain(curve_id)
    
    r1_param = domain[0] + (parameter * (domain[1] - domain[0]))# slice curve domain
    r3point = rs.EvaluateCurve(curve_id, r1_param) # at each domain chunk, store a var
    if r3point:
        point_id = rs.AddPoint(r3point) # add new point object along each domain chunk
        rs.ObjectColor(point_id, paramColor(parameter)) # color each point with a incrementing param
        
def paramColor(parameter):
    red = 255 * parameter # set var to 255 * incrementor
    if red < 0: # catch edges
        red = 0
    if red > 255: # catch edges
        red = 255 
    return(red, 0, 255-red) # return rgb values - (red, 0, stepping towards red)
    
main()