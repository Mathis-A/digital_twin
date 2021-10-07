import numpy as np
class Wall:
    def __init__(self,p1,p2):
        self.points=(p1,p2)

    def get_coordinates(self):
        return (self.points)

    def size(self):
        return np.sqrt( (self.points[0][0]-self.points[1][0])**2 + 
                        (self.points[0][1]-self.points[1][1])**2 )
