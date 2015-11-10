# modified from RhinoPythonPrimer Rev3
import rhinoscriptsyntax as rs
import time

rs.AddCone((0,0,0), 10, 5, True)

strObjectID = rs.GetObject("select an obj to rename", 0, False, True)

if strObjectID:
    strNewName = "Time: " + str(time.localtime())
    rs.ObjectName(strObjectID, strNewName)
    # alt = rs.ObjectName(strObjectID, "time: " & str(time.localtime()))
    print strNewName