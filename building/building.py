from numpy.lib.arraysetops import isin
from area.area import Area
from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
import numpy as np

class Building:
    def __init__(self,name='default'):
        self.name=name
        self.floors=1
        self.areas=[[]]

        self.floor_height=3

    def addAreas(self,areas,floor=0):
        if not isinstance(areas,list):
            areas=[areas]
        for a in areas:
            assert isinstance(a, Area)
        assert floor<=self.floors
        for area in areas:
            self.areas[floor].append(area)

    def addFloor(self,n=1):
        assert n>=1
        self.floors+=n
        for i in range(n):
            self.areas.append([])

    def show(self,floor='all'):
        
        if isinstance(floor,int):
            to_show=self.areas[floor-1]
            h=self.floor_height*(floor-1)
        else:
            to_show=self.areas
        
        to_show=self.areas
        fig = plt.figure(figsize=(6,6))
        ax = fig.add_subplot(111, projection='3d')

        verts=[]
        h=[]

        for f in range(len(to_show)):
            for a in to_show[f]:
                points=a.points #a corresponds to the i-th area in (object) floor to_show[f]
                verts.append(points)
                h.append(self.floor_height*f)

        colors=[]
        while len(colors)<len(verts)-2:
            colors+=['r','b','g']
        if len(colors)<len(verts):
            colors.append('r')
        if len(colors)<len(verts):
            colors.append('b')

        poly=PolyCollection(verts,facecolors=colors)
        poly.set_alpha(0.7)
        ax.add_collection3d(poly,zs=h)

        xmin,ymin=to_show[0][0].points[0]
        xmax,ymax=xmin,ymin
        for a in to_show[0]:
            xmin=min(min(np.array(a.points)[:,0]),xmin)
            ymin=min(min(np.array(a.points)[:,0]),ymin)
            xmax=max(max(np.array(a.points)[:,0]),xmax)
            ymax=max(max(np.array(a.points)[:,0]),ymax)

        h_max=np.array(self.floor_height*len(self.areas))
        ax.set_xlim3d(xmin, xmax)
        ax.set_ylim3d(ymin, ymax)
        ax.set_zlim3d(0, h_max+1)
        plt.show()
            



    def change_name(self,name):
        self.name=name