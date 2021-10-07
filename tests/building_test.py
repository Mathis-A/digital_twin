from area.area import Area 
from walls.walls import Wall

import unittest

class BuildingTest(unittest.TestCase):
    
    def test_wall_size(self):
        w1=Wall((0,0),(3,4))
        self.assertEqual(w1.size(),5)

    def test_size(self):
        ar=Area((0,0),(2,3))
        self.assertEqual(ar.size(),6)

