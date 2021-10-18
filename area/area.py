import numpy as np
from numpy.core.shape_base import hstack
from walls.walls import Wall


class Area:
    """
        Creates an convex area from the given points
    """
    def __init__(self,points): 
        """
        Parameters
        ----------
        points : List
            Coordinates (x,y) of points that will create the Area by taking the hull
        """
        points=np.array(points)

        assert len(points)>2
        assert points.shape[1]==2
        assert len(points.shape)==2

        self.points=self.convexHull(points)
        self.walls=[Wall(self.points[i],self.points[i+1]) for i in range(len(self.points)-1)]
        self.walls.append(Wall(self.points[-1],self.points[0]))
        self.coordinates=list(np.array(self.points).flatten()) # x1,y1,x2,y2,x3,y3...
    
    def convexHull(self,points):
        """ Computes the convex hull of a given set of points in 2D

        Parameters
        ----------
        points : List
            coordinates in the form of a tuple : [(x1,y1),(x2,y2),...]

        Returns
        -------
        List
            coordinates of the hull, ordered counter clockwise
        """
        #bad way of taking the lower left-est point 
        pos_pivot=0
        pivot=min(sorted(points,key=lambda p:p[0]), key=lambda p:p[1])

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
        """ Computes the area of the object

        Returns
        -------
        int
            Area of the object
        """
        cum_sum=0
        offset=abs(min(self.coordinates))+1 #every point is above the x axis
        for w in self.walls:
            x1,y1,x2,y2=w.coordinates
            cum_sum-=(x2-x1)*(y1+offset+y2+offset)/2 #substract because counter-clockwise
        return cum_sum

    def inside(self,pos):
        """Checks if pos is in the object

        Parameters
        ----------
        pos : tuple of size 2
            Coordinates of the point to check

        Returns
        -------
        boolean
            whether pos is in the object
        """
        new_hull=self.convexHull(self.points+[pos])
        print(new_hull)
        return new_hull==self.points

class Room(Area):
    def __init__(self,points):
        super().__init__(points)