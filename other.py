from area.area import Area, Room
from building.building import Building
from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

ar1=Area([(0,0),(2,0),(2,3),(0,3)])
ar2=Area([(2,0),(5,0),(5,3),(2,3)])
ar3=Room([(0,0),(0,3),(3,3)])
ar4=Area([(0,0),(5,0),(5,3),(3,3)])
ar5=Room([(2.5,0),(5,0),(5,3),(2.5,3)])
b=Building('MyBuilding')
b.addAreas([ar1,ar2],0)
b.addFloor()
b.addFloor()
b.addAreas([ar3,ar4],1)
b.addAreas(ar5,2)

b.show()