import unittest
from area.area import Area, Room
from walls.walls import Wall
from building.building import Building
from IPS.ips import IPS

# python -m unittest tests/building_test.py in terminal
class IpsTest(unittest.TestCase):
    def test_create_ips(self):
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
        ips=IPS(b)
        self.assertEqual(b,ips.building)