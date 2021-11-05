import random as rd
import matplotlib
from matplotlib import cm
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

class IPS():
    def __init__(self,building):
        self.building=building
        self.clients=[]
        self.history=[[]]
    
    def add_client(self,n=1,c=None):
        """Adds 'clients' : a point that will wander in the building

        Parameters
        ----------
        n : int, optional
            number of clients to add, by default 1
        c : list, optional
            coordinates to start with, has to be of size n, random by default 
        """
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
            self.history[-1].append(c[i])
    
    def move_clients(self):
        """Iterates once the clients : moves in a random direction
        """
        delta=0.1
        for i in range(len(self.clients)):
            floor=self.clients[i][-1]
            new_position=(self.clients[i][0]+(2*rd.random()-1)*delta,self.clients[i][1]+(2*rd.random()-1)*delta,floor)
            while len(self.building.position(new_position))==0:
                new_position=(self.clients[i][0]+(2*rd.random()-1)*delta,self.clients[i][1]+(2*rd.random()-1)*delta,floor)
            self.clients[i]=new_position
            

    def sample_clients(self,n=1,time=10):
        """Creates clients and iterates them

        Parameters
        ----------
        n : int, optional
            number of clients, by default 1
        time : int, optional
            number of iterations to be done, by default 10
        """
        self.add_client(n=n)
        for _ in range(time-1):
            self.move_clients()
            self.history.append(self.clients.copy())
    
    def show_clusters(self,n_clusters,floor=0):
        """Plots the different positions of the clients and groups them by KMeans clustering

        Parameters
        ----------
        n_clusters : int
            number of clusters to use
        floor : int, optional
            floor to monitor, by default 0
        """
        X=np.concatenate(self.history)
        X_floor=X[X[:,2]==floor][:,:2] #coordinates (x,y) of points in desired floor
        Y = KMeans(n_clusters=n_clusters,random_state=0).fit_predict(X_floor)
        plt.scatter(x=X_floor[:,0],y=X_floor[:,1],c=Y)
        plt.show()
    
    def heatmap(self,n_clusters,floor=0):
        """functions that shows each area with a colour depending on population 

        """
        X=np.concatenate(self.history)
        X_floor=X[X[:,2]==floor][:,:2] #coordinates (x,y) of points in desired floor
        kmean = KMeans(n_clusters=n_clusters,random_state=0).fit(X_floor)
        Y = kmean.predict(X_floor)
        centers = kmean.cluster_centers_
        name, size = np.unique(Y, return_counts=True)
        lala = cm.get_cmap('magma',len(name))
        print(lala)
        plt.axis([np.min(X_floor[:,0]),np.max(X_floor[:,0]),np.min(X_floor[:,1]),np.max(X_floor[:,1])])
        for i in range(len(centers)):
            plt.gca().add_artist(plt.Circle((centers[i][0],centers[i][1]),radius=0.1,color=lala(size[i]/np.sum(size))))    
        plt.show()