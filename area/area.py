from walls.walls import Wall

class Area:
    def __init__(self,corner1,corner2): #corner is supposed to be [x1,x2] where x1, x2 are the bottom left and the upper right 
        """
        Parameters
        ----------
        corner : List
            List containing 2 elements representing the coordinates defining the rectangle
        """

        assert len(corner1)==2        # consisting of 2 coordinates
        assert len(corner2)==2

        assert corner1[0]!=corner2[0]   #the area is not of length or width != 0
        assert corner1[1]!=corner2[1]

        self.corner=(corner1,corner2)

    def get_coordinates(self):
        return (self.corner)
    
    def get_walls(self):
        corn1=self.corner[0]
        corn2=self.corner[1]
        corn3=(corn1[0],corn2[1])
        corn4=(corn2[0],corn1[1])
        return (Wall(corn1,corn3),Wall(corn3,corn2),Wall(corn2,corn4),Wall(corn4,corn1))
    
    def size(self):
        return (self.corner[0][0]-self.corner[1][0])*(self.corner[0][1]-self.corner[1][1])

class Room(Area):
    def __init__(self,corner):
        super().__init__(corner)