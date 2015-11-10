# make random cylinders based on user input count
# the example made this waay harder than it had to be!

import rhinoscriptsyntax as rs
import math
import random

def CreateCircle():
    # user input for sizes
    # center = rs.GetPoint("Center point of circle")
    total_num = rs.GetInteger("total number of circs? ")
    
    for i in range(total_num):
        x = random.randint(-30,30)
        y = random.randint(-30,30)
        z = random.randint(0,15)
        radius = random.randint(5, 20)
        height = random.randint(5,50)
        objectID = rs.AddCylinder((x, y, z), height, radius)
        print objectID
        # GUIDs are messy long strings!!!
        # remember a return will end ur loop!
        # rs.SelectObject(objectId) will select/rhino highlight this object

CreateCircle()

# rs.SetObjectData :: this might be the jam? "set" is the language in gh.
# i think the sauce is in "rs.GetObject" like number input but of geo type.
