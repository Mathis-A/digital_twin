import numpy as np
class Wall:
    def __init__(self,p1,p2):
        self.points=(p1,p2)
        self.coordinates=(p1[0],p1[1],p2[0],p2[1])

    def size(self): #TODO Move to Element class tbd
        """ Computes the length of the object

        Returns
        -------
        int
            length of the object
        """
        return np.sqrt( (self.points[0][0]-self.points[1][0])**2 + 
                        (self.points[0][1]-self.points[1][1])**2 )
