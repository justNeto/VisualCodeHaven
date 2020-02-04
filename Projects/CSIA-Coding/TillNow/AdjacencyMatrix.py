import math
import numpy as np
import networkx as nx

class Vertex:

    def __init__(self, vertexName, x_cor, y_cor):
        if isinstance(vertexName, str) and isinstance(x_cor, int) and isinstance(y_cor, int):
            self.name = vertexName # name of the Node, also could be considered as a label :)
            self.location = [x_cor, y_cor] # x and y coordinates of the node inside the map image
        else:
            return False


class Graph:
    
    vertices = {}
    edges = np.empty([])
    indices = {}
    
    def add_vertex(self, vertexName):
        self.vertices[vertexName.name] = vertexName.location

    def set_weights(self, vertexOne, vertexTwo):
        dis = math.sqrt(((self.vertices[vertexOne][1] - self.vertices[vertexTwo][1])**2) + 
            ((self.vertices[vertexOne][0] - self.vertices[vertexTwo][0])**2))
        return dis

    def add_edge(self, vertexOne, vertexTwo):
        j = 0
        for keys in self.vertices:
            self.indices[keys] = j
            j += 1
        self.edges[self.indices[vertexOne]][self.indices[vertexTwo]] = self.set_weights(vertexOne, vertexTwo)
        self.edges[self.indices[vertexTwo]][self.indices[vertexOne]] = self.set_weights(vertexOne, vertexTwo)

    def init_matrix(self):
        self.edges = np.zeros((len(self.vertices), len(self.vertices)))

    def get_vertices(self):
        print(self.vertices)

    def get_indices(self):
        print(self.indices)

    def get_matrix(self):
        print(self.edges)
    
    
'''def DijstrakAlgorithm(graph, origin, target):
    for key in graph.indices:
        if key == origin:
            actIndexOr = graph.indices[key]
        if key == target:
            actIndexDest = graph.indices[key]
        end = nx.from_numpy_matrix(graph.edges, create_using=nx.DiGraph())
        print(nx.dijkstra_path(end,actIndexOr, actIndexDest)   
'''

g = Graph()
g.add_vertex(Vertex('A', 12,18))
g.add_vertex(Vertex('B', 15, 29))
g.add_vertex(Vertex('C', 19, 12))
g.add_vertex(Vertex('D', 29, 41))
g.add_vertex(Vertex('F', 33, 31))

g.init_matrix()

g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('C', 'D')
g.add_edge('F', 'A')
        

g.get_matrix()
print('\n')
g.get_indices()
print('\n')

