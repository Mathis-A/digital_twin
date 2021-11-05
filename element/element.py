import numpy as np

class Element:
    def __init__(self,p1,p2):
        '''
        p1 and p2 are points (two-item list) of the plane that defines a segment representing the element. We consider its thickness
        to be null and we work in 2D (view from above)
        '''
        self.coordinates=[p1,p2]

    def size(self):
        """ Computes the size of the element

        Returns
        -------
        int
            length of the object
        """
        return np.sqrt( (self.coordinates[0][0]-self.coordinates[1][0])**2 + 
                        (self.coordinates[0][1]-self.coordinates[1][1])**2 )
