import unittest
from area.area import Area, Room
from building.building import Building
from IPS.ips import IPS

# python -m unittest tests/ips_test.py in terminal
class IpsTest(unittest.TestCase):
    def test_building(self):
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
        return b
    
    def test_create_ips(self):
        b=self.test_building()
        ips=IPS(b)
        self.assertEqual(b,ips.building)

    def test_add_client(self):
        b=self.test_building()
        ips=IPS(b)
        ips.add_client(n=5)
        self.assertEqual(5,len(ips.clients))
    
    def test_add_client_by_coordinates(self):
        b=self.test_building()
        ips=IPS(b)
        ips.add_client(n=1,c=[(0,0,0)])
        self.assertEqual((0,0,0),ips.clients[0])
    
    def test_move_clients(self):
        b=self.test_building()
        ips=IPS(b)
        ips.add_client(n=2,c=[(0,0,0),(0,0,1)])
        ips.move_clients()
        self.assertNotEqual(ips.clients,[(0,0,0),(0,0,1)])

    def test_sample_random_walks(self):
        b=self.test_building()
        ips=IPS(b)
        ips.sample_clients(n=5,time=20)
        self.assertEqual(len(ips.history),20)
        self.assertEqual(len(ips.history[0]),5)
    
    def test_clusters(self):
        b=self.test_building()
        ips=IPS(b)
        ips.sample_clients(n=10,time=50)
        ips.show_clusters(4)
    
    def test_heatmap(self):
        b=self.test_building()
        ips=IPS(b)
        ips.sample_clients(n=10,time=50)
        ips.heatmap(4)