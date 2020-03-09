from copy import copy
import sys
import math
import numpy as np

class Vertex: # class vertex for creating objects with x, y values

    def __init__(self, vertexName, x_cor, y_cor):
        if isinstance(vertexName, str) and isinstance(x_cor, int) and isinstance(y_cor, int):
            self.name = vertexName # name of the Node, also could be considered as a label :)
            self.location = [x_cor, y_cor] # x and y coordinates of the node inside the map image
        else:
            return "You are doing something wrong"
            return False # sends a warning


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
        stack = list()
        y = tar
        if prev[y] != None or y != org:
            while y != None:
                stack.append(y)
                y = prev[y]
        stack = stack[::-1]
        return stack
"""
THIS IS THE STRUCTURE FOR CREATING THE GRAPH AND ALGORITHMS:

----------------------- CREATE Graph OBJECT--------------------------

graphName = Graph()

----------------------- ADDING Vertex OBJECTS ----------------------- 

NameOfVertex = Vertex('NAME', x_coor, y_coor)

--------------- ADDING Vertex OBJECTS to GRAPH OBJECT ---------------

graphName.add_vertex(NameOfVertex)

------------------------------- OR ----------------------------------

graphName.add_vertex(NameOfVertex('NAME',x_coor, y_coor)

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
