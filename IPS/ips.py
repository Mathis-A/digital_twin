import random as rd

class IPS():
    def __init__(self,building):
        self.building=building
        self.clients=[]
    
    def add_client(self,n=1,c=None):
        if not c:
            c=[]
            for i in range(n):
                floor=rd.choice(range(self.building.floors))
                areas=self.building.areas[floor]
                starting_area=rd.choice(areas)
                starting_point=rd.choice(starting_area.points)
                c.append((starting_point[0],starting_point[1],floor))

        for i in range(n):            
            self.clients.append(c[i])
    
    def move_clients(self):
        delta=0.1
        for i in range(len(self.clients)):
            floor=self.clients[i][-1]
            new_position=(self.clients[i][0]+(2*rd.random()-1)*delta,self.clients[i][1]+(2*rd.random()-1)*delta,floor)
            print(new_position)
            while len(self.building.position(new_position))==0:
                new_position=(self.clients[i][0]+(2*rd.random()-1)*delta,self.clients[i][1]+(2*rd.random()-1)*delta,floor)
            self.clients[i]=new_position

    def sample_clients(self,n=1,time=10):
        self.add_client(n=n)
        history=[self.clients]
        for _ in range(time-1):
            self.move_clients()
            history.append(self.clients)
        return history


