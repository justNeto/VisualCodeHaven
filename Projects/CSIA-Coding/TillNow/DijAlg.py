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

    def set_matrix(self):
        for i in range(len(self.edges)):
            for j in range(len(self.edges)):
                if i !=j and self.edges[i][j] == 0:
                    self.edges[i][j] = 1000

    def get_vertices(self): # gets the value of the vertices
        print(self.vertices)

    def get_indices(self): # gets the indices of the vertices
        print(self.indices)

    def get_matrix(self): # gets the matrix
        print(self.edges)

    def alg(self, org): # the actual dijstrak algorithmn
        vertSet = set() # empty python set
        dist = dict() # empty distv dict
        listAux = list()
        for key in self.indices: # this checks for the values inside the vertices dictionary and 
            # sets a prior, infinite distance for distv and an undefined prior distance for the prevv
            dist[key] = 1000
            vertSet.add(key) # this adds to the vertex's set each vertex
        dist[org] = 0 # this sets the original vertex's distance to 0
        print(vertSet)
        print(dist)

g = Graph()
g.add_vertex(Vertex('A', 12,18))
g.add_vertex(Vertex('B', 15, 29))
g.add_vertex(Vertex('C', 19, 12))
g.add_vertex(Vertex('D', 29, 41))
g.add_vertex(Vertex('E', 33, 31))
g.add_vertex(Vertex('F', 12, 15))

g.init_matrix()

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('C', 'D')
g.add_edge('C', 'E')
g.add_edge('E', 'F')
g.add_edge('D', 'F')
        
g.set_matrix()

print("This is the adjacency matrix:\n")
g.get_matrix() # or get edges / weights between the vertices
print('\nAnd these are the adjacency matrix indices with respect to their position in the matrix(self.indices):\n')
g.get_indices() # get the vertices' index with respect to their position in the graph
print('\nThese are the vertices in an ordered manner with their x and y locations (self.vertices):\n')
g.get_vertices() # these are the vertices with their x and y locations
print('\n')

g.alg('C')
