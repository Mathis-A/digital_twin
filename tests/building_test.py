from area.area import Area, Room
from element.walls import Wall
from building.building import Building


import unittest

# python -m unittest tests/building_test.py in terminal
class BuildingTest(unittest.TestCase):
    
    def test_wall_size(self):
        w1=Wall((0,0),(3,4))
        self.assertEqual(w1.size(),5)

    def test_size(self):
        ar=Area([(0,0),(2,0),(2,3),(0,3)])
        self.assertEqual(ar.size(),6)

    def test_convex(self):
        points=[(0,0),(2,0),(2,3),(0,3)]
        ar=Area(points+[(1,1)])
        self.assertEqual(set(ar.points),set(points))

    def test_position_area(self):
        ar=Area([(0,0),(2,0),(2,3),(0,3)])
        pos=(1.5,2.8)
        self.assertTrue(ar.inside(pos))
    
    def test_size2(self):
        ar=Area([(0,0),(2,3),(2,0),(0,3)])
        self.assertEqual(ar.size(),6)

    def test_describe_building(self):
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
        self.assertEqual(b.floors,3)
        self.assertEqual(b.areas,[[ar1,ar2],[ar3,ar4],[ar5]])

    def test_show(self):
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