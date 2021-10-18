import numpy as np
from numpy.core.shape_base import hstack
from walls.walls import Wall


class Area:
    """
        Creates an convex area from the points given
    """
    def __init__(self,points): 
        """
        Parameters
        ----------
        corner : List
            List containing elements representing the coordinates defining the area
        """
        points=np.array(points)

        assert len(points)>2
        assert points.shape[1]==2
        assert len(points.shape)==2

        self.points=self.convexHull(points)
        self.walls=[Wall(self.points[i],self.points[i+1]) for i in range(len(self.points)-1)]+[
                    Wall(self.points[-1],self.points[0])]
        self.coordinates=list(np.array(self.points).flatten()) # x1,y1,x2,y2,x3,y3...
    
    def convexHull(self,points):
        pos_pivot=0
        for i in range(1,len(points)):
            if points[i][1]<points[pos_pivot][1]:
                pos_pivot=i
            elif points[i][1]==points[pos_pivot][1]:
                if points[i][0]<points[pos_pivot][0]:
                    pos_pivot=i
        pivot=points[pos_pivot]

        # sort with pivot at first pos
        points=np.delete(points,pos_pivot,axis=0)
        sorted_points=sorted(points, key=lambda p:np.sqrt(p[0]**2+p[1]**2))
        offset=abs(points.min())+1 #so that all coordinates are positive
        sorted_points=sorted(sorted_points, key=lambda p:(p[1]+offset)/(p[0]+offset))
        sorted_points=np.vstack([pivot,sorted_points])

        #create list on points of the convex hull 
        ccw = lambda p1,p2,p3 : (p2[0]-p1[0])*(p3[1]-p1[1])-(p2[1]-p1[1])*(p3[0]-p1[0])
        convex_points=[]
        for point in sorted_points:
            while len(convex_points) > 1 and ccw(convex_points[-2], convex_points[-1], point) <= 0:
                convex_points.pop()
            convex_points.append((point[0],point[1]))
        
        return convex_points

    def size(self):
        cum_sum=0
        offset=abs(min(self.coordinates))+1
        for w in self.walls:
            x1,y1,x2,y2=w.coordinates
            cum_sum-=(x2-x1)*(y1+offset+y2+offset)/2 #substract because the hull goes around counter-clockwise
        return cum_sum

    def inside(self,pos):
        new_hull=self.convexHull(self.points+[pos])
        print(new_hull)
        return new_hull==self.points

class Room(Area):
    def __init__(self,points):
        super().__init__(points)