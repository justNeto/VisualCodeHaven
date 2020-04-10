from copy import copy
import sys
import math
import numpy as np

class Vertex: # class vertex for creating objects with x, y values

    def __init__(self, vertexName, x_cor, y_cor):
        self.name = vertexName # name of the Node, also could be considered as a label :)
        self.location = [x_cor, y_cor] # x and y coordinates of the node inside the map image


class Graph: # class graph creates a graph with a given number of vertices and allows to add weights
    
    vertices = {} # dictionary for the name of each vertes and their [x, y] coordinates
    edges = np.empty([]) # the numpy matrix which is actually the Adjacency Matrix that is used for dijstrak algorithm
    indices = {} # dictionary that contains the relative position of the vertices' values inside the adjacency matrix
    
    def add_vertex(self, vertexName): # add vertex to the vertices dictionary and their [x, y] coordinate
        self.vertices[vertexName.name] = vertexName.location

    def set_weights(self, vertexOne, vertexTwo): # assumin the nodes are all connected in a straight line
        # it computes their euclidean distance
        dis = math.sqrt(((self.vertices[vertexOne][1] - self.vertices[vertexTwo][1])**2) + ((self.vertices[vertexOne][0] - self.vertices[vertexTwo][0])**2))
        return dis

    def add_edge(self, vertexOne, vertexTwo): # adds a distance between two vertices inside the matrix
        j = 0
        for keys in self.vertices:
            self.indices[keys] = j
            j += 1
        self.edges[self.indices[vertexOne]][self.indices[vertexTwo]] = self.set_weights(vertexOne, vertexTwo)
        self.edges[self.indices[vertexTwo]][self.indices[vertexOne]] = self.set_weights(vertexOne, vertexTwo)

    def init_matrix(self): # after adding all the relationships between matrices, it initiazes the matrix
        self.edges = np.zeros((len(self.vertices), len(self.vertices)))

    def get_vertices(self): # gets the value of the vertices
        print(self.vertices)

    def get_indices(self): # gets the indices of the vertices
        print(self.indices)

    def get_matrix(self): # gets the matrix
        print(self.edges)
    
    def alg(self, org, tar): # the actual dijstrak algorithmn
        vertSet = set() # empty python set
        dist = dict() # empty distv dict
        distAux = dict()
        prev = dict() # empty prevv dict
        tarReached = False
        u_def = False

        for key in self.indices: # this checks for the values inside the vertices dictionary and 
            # sets a prior, infinite distance for distv and an undefined prior distance for the prevv
            dist[key] = 1000
            prev[key] = None
            vertSet.add(key) # this adds to the vertex's set each vertex
        dist[org] = 0 # this sets the original vertex's distance to 0
        distAux = copy(dist)

        while vertSet != 0 and tarReached == False:
            listAux = list()
            for key in dist:
                listAux.append(dist[key])
            listAux.sort()
            while u_def != True:
                minDist = listAux[0]
                u = [key for (key, value) in dist.items() if value == minDist]
                u = "".join(u)
                if u in vertSet:
                    u_ref = [value for (key, value) in self.indices.items() if key == u]
                    u_ref = np.asscalar(np.asarray(u_ref))
                    vertSet.remove(u)
                    break
                else:
                    listAux.pop(0)
                    u = list()
            # u makes reference to the node we are currently using
            # we should always take u as the reference for the algorithm
            # dist[u] is the value of the distance inside the dist dict, for the 'u' key
            aux2 = ((np.asarray(np.where(self.edges[u_ref] != 0))).flatten()).tolist()
            if u == tar:
                tarReached = True

            for i in range(len(self.edges[u_ref])):
                # but u should be the value for the key u in self.indices
                if self.edges[u_ref][i] != 0: 
                # if v is not 0 and v is in setVert
                    aux3 = aux2.pop()
                    v = [key for (key, value) in self.indices.items() if value == aux3] # probar esto
                    v = "".join(v)
                    if v in vertSet: 
                        alt = minDist + self.edges[u_ref][i] #blength(u, v)
                        # value of dist for v
                        if alt < dist[v]:
                            dist[v] = alt
                            prev[v] = u
        lastList = list()
        y = tar
        if prev[y] != None or y != org:
            while y != None:
                lastList.append(y)
                y = prev[y]
        lastList = lastList[::-1]
        return lastList
"""
THIS IS THE STRUCTURE FOR CREATING THE GRAPH AND ALGORITHMS:
----------------------- CREATE Graph OBJECT--------------------------
graphName = Graph()
----------------------- ADDING Vertex OBJECTS ----------------------- 
NameOfVertex = Vertex('NAME', x_coor, y_coor)
--------------- ADDING Vertex OBJECTS to GRAPH OBJECT ---------------
graphName.add_vertex(NameOfVertex)
------------------------------- OR ----------------------------------
graphName.add_vertex(Vertex('NAME',x_coor, y_coor)
---------------------- INIT MATRIX AND WEIGHTS ----------------------
graphName.init_matrix()
graphName.add_edge('NameOfVertexOne, 'NameOfVertexTwo')
----------------------- OTHER METhODS (PRIVATE) ---------------------
graphName.get_matrix()  -> get edges / weights between the vertices
graphName.get_indices() -> get the vertices' index with respect to their position in the graph
graphName.get_vertices()-> these are the vertices with their x and y locations
---------------------------DIJSKTRAK ALGORITHM --------------------------
 
 graphName.dijs('NameOfVertexOne', 'NameOfVertexTwo')
---------------------------------------------------------------------------
"""

g = Graph()
g.add_vertex(Vertex('Foldio',8.45, 6.23))
g.add_vertex(Vertex('Otros/others',13.09,6.26))
g.add_vertex(Vertex('Sala de maestros/teachers lounge',21.10, 6.38))
g.add_vertex(Vertex('A5', 27.39,6.31))
g.add_vertex(Vertex('Al',25.42,9.17))
g.add_vertex(Vertex('Sanitarios/restrooms 1',29.80, 6.06))
g.add_vertex(Vertex('Transportec',27.45,11.52))
g.add_vertex(Vertex('Ak',25.54,13.16))
g.add_vertex(Vertex('Aj',22.94,13.07))
g.add_vertex(Vertex('Ai',20.48,13.15))
g.add_vertex(Vertex('Ag',18.02,13.12))
g.add_vertex(Vertex('Ah',18.02,9.72))
g.add_vertex(Vertex('Ad',15.70,10.99))
g.add_vertex(Vertex('Ab',15.58,13.15))
g.add_vertex(Vertex('A1',14.76,15.33))
g.add_vertex(Vertex('A2',19.29,15.37))
g.add_vertex(Vertex('A3', 24.70,15.32))
g.add_vertex(Vertex('Ac',13.16,13.08))
g.add_vertex(Vertex('Af',13.13,9.27))
g.add_vertex(Vertex('A4',27.49,15.30))
g.add_vertex(Vertex('T1',31.77,7.94))
g.add_vertex(Vertex('T2',31.85,10.45))
g.add_vertex(Vertex('M1',29.95,12.06))
g.add_vertex(Vertex('P3',33.31,11.43))
g.add_vertex(Vertex('Usos multiples/multiple uses',32.86,9.81))
g.add_vertex(Vertex('M2',27.49,18.62))
g.add_vertex(Vertex('M3',27.49,21.80))
g.add_vertex(Vertex('Labs/Locatec',34.18,6.06))
g.add_vertex(Vertex('P2',33.29,19.13))
g.add_vertex(Vertex('P1',33.31,25.93))
g.add_vertex(Vertex('D3',35.34,19.29))
g.add_vertex(Vertex('E1',29.61,22.92))
g.add_vertex(Vertex('E2',29.84,33.46))
g.add_vertex(Vertex('E3',33.32,31.26))
g.add_vertex(Vertex('E4',32.41,36.49))
g.add_vertex(Vertex('O1',27.49,36.47))
g.add_vertex(Vertex('E5',32.31,38.39))
g.add_vertex(Vertex('E6',32.57,40.56))
g.add_vertex(Vertex('E7',29.18,39.79))
g.add_vertex(Vertex('O2',32.35,42.24))
g.add_vertex(Vertex('Cajeros/ATM/Oficinas Life/Lifes Office',34.42,44.49))
g.add_vertex(Vertex('Cancha de baloncesto/Basket court',35.17,41.48))
g.add_vertex(Vertex('C2',37.85,26.94))
g.add_vertex(Vertex('C5',37.19,28.34))
g.add_vertex(Vertex('C1',40.60,26.85))
g.add_vertex(Vertex('C3',43.02,26.82))
g.add_vertex(Vertex('C4',44.26,28.32))
g.add_vertex(Vertex('D5',40.56,22.01))
g.add_vertex(Vertex('D2',40.61,19.31))
g.add_vertex(Vertex('D3',35.25,19.26))
g.add_vertex(Vertex('D4',45.87,19.26))
g.add_vertex(Vertex('D1',40.59,14.20))
g.add_vertex(Vertex('P4',40.59,11.31))
g.add_vertex(Vertex('P5',46.32,11.44))
g.add_vertex(Vertex('P6',46.86,17.05))
g.add_vertex(Vertex('T3',48.56,12.34))
g.add_vertex(Vertex('F1',48.80,16.88))
g.add_vertex(Vertex('F2',48.59,21.87))
g.add_vertex(Vertex('F3',51.27,21.62))
g.add_vertex(Vertex('F4',53.67,21.72))
g.add_vertex(Vertex('H1',48.69,25.89))
g.add_vertex(Vertex('H3',49.74,30.92))
g.add_vertex(Vertex('H2',48.39,31.62))
g.add_vertex(Vertex('H4',53.21,30.91))
g.add_vertex(Vertex('H5',53.62,29.67))
g.add_vertex(Vertex('H6',53.57,27.50))
g.add_vertex(Vertex('F5',53.62,16.60))
g.add_vertex(Vertex('F6',53.62,13.50))
g.add_vertex(Vertex('F7',56.35,12.55))
g.add_vertex(Vertex('F8',57.53,14.25))
g.add_vertex(Vertex('Canchas de Tenis', 58.19,15.37))
g.add_vertex(Vertex('Sanitarios/restrooms 3',59.97,12.35))
g.add_vertex(Vertex('Enfermeria/Infirmary',59.75,8.35))
g.add_vertex(Vertex('Oxxo',52.53,12.18))

g.init_matrix()

g.add_edge('P3','P2')
g.add_edge('P2','P1')
g.add_edge('P1','E3')
g.add_edge('P3','P4')
g.add_edge('P4','P5')
g.add_edge('P5','T3')
g.add_edge('T3','F6')
g.add_edge('FE','F7')
g.add_edge('F7','F8')
g.add_edge('F8','F6')
g.add_edge('F6','F5')
g.add_edge('F8','F5')
g.add_edge('F5','F4')
g.add_edge('F4','H6')
g.add_edge('H6','H5')
g.add_edge('H5','H4')
g.add_edge('H4','H3')
g.add_edge('H3','H2')
g.add_edge('H2','H1')
g.add_edge('H1','F2')
g.add_edge('F2','F1')
g.add_edge('F1','T3')
g.add_edge('F2','F3')
g.add_edge('F3','F4')
g.add_edge('H3','H1')
g.add_edge('P5','P6')
g.add_edge('P6','T3')
g.add_edge('P6','F1')
g.add_edge('P6','F2')
g.add_edge('P6','H1')
g.add_edge('P6','H2')
g.add_edge('P6','D4')
g.add_edge('D4','F1')
g.add_edge('D4','F2')
g.add_edge('D4','H1')
g.add_edge('D4','H2')
g.add_edge('D4','H3')
g.add_edge('D4','P5')
g.add_edge('P5','P4')
g.add_edge('P4','D1')
g.add_edge('D1','D2')
g.add_edge('D2','D4')
g.add_edge('D2','D5')
g.add_edge('D5','C1')
g.add_edge('C1','C3')
g.add_edge('C3','C4')
g.add_edge('C1','C2')
g.add_edge('C2','C5')
g.add_edge('E3','E2')
g.add_edge('E2','E4')
g.add_edge('E4','E5')
g.add_edge('E5','E6')
g.add_edge('E6','O2')
g.add_edge('O2','E7')
g.add_edge('E7','E4')
g.add_edge('E7','E5')
g.add_edge('E7','E2')
g.add_edge('E7','O1')
g.add_edge('O1','E2')
g.add_edge('E2','E3')
g.add_edge('E2','M3')
g.add_edge('M3','M2')
g.add_edge('M2','A4')
g.add_edge('O2','Cancha de baloncesto/Basketball court')
g.add_edge('O2','Cajeros/ATM/Oficinas Life/Lifes Office')
g.add_edge('F8','Canchas de Tenis')
g.add_edge('F8','Sanitarios/restrooms 3')
g.add_edge('F7','Sanitarios/restrooms 3')
g.add_edge('F7','Oxxo')
g.add_edge('F6','Oxxo')
g.add_edge('T3','Oxxo')
g.add_edge('F7','Enfermeria/Infirmary')
g.add_edge('F8','Enfermeria/Infirmary')
g.add_edge('T1','Usos multiples/multiples uses')
g.add_edge('T2','Usos multiples/multiples uses')
g.add_edge('P3','Usos multiples/multiples uses')
g.add_edge('T1','Sanitarios/restrooms 1')
g.add_edge('T1','Labs/Locatec')
g.add_edge('A5','Labs/Locatec')
g.add_edge('A5','Sanitarios/restrooms 1')
g.add_edge('P4','Labs/Locatec')
g.add_edge('Foldio','Otros/others')
g.add_edge('Foldio','Af')
g.add_edge('Foldio', 'Ah')
g.add_edge('Otros/others','Af')
g.add_edge('Otros/others', 'Ah')
g.add_edge('Otros/others','Ad')
g.add_edge('Otros/others','Sala de maestros/teachers lounge')
g.add_edge('Af','Ah')
g.add_edge('Af','Ac')
g.add_edge('Ac','Ab')
g.add_edge('Ac','A1')
g.add_edge('Ab','Ad')
g.add_edge('Ad','Ah')
g.add_edge('Ah','Ag')
g.add_edge('A1','A2')
g.add_edge('A2','Ag')
g.add_edge('A2','Ai')
g.add_edge('A2','A3')
g.add_edge('A3','Aj')
g.add_edge('Aj','Sala de maestros/teachers lounge')
g.add_edge('Sala de maestros/teachers lounge','Al')
g.add_edge('Sala de maestros/teachers lounge','A5')
g.add_edge('Al','Ak')
g.add_edge('Aj','Ak')
g.add_edge('A3','Ak')
g.add_edge('A3','A4')
g.add_edge('A4','Ak')
g.add_edge('A4','Transportec')
g.add_edge('Transportec','A5')
g.add_edge('A5','Sanitarios/restrooms 1')
