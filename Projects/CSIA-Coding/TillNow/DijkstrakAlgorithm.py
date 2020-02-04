from AdjacencyList import g
import networkx as nx

matrix = [[ 0.0, 11.40175425, 0.0, 0.0, 24.69817807],                  
[11.40175425, 0.0, 17.4642492, 0.0, 0.0],                     
[ 0.0, 17.4642492, 0.0, 30.6757233, 0.0],                     
[ 0.0, 0.0, 30.6757233, 0.0, 0.0],                            
[24.69817807, 0.0, 0.0, 0.0, 0.0]]                              

def DijkstrakAlgorithm(graph, origin, destination):
    for key in graph.indices:
        if key == origin:
            actIndexOrigin = graph.indices[key]
        if key == destination:
            actIndexDestination = graph.indices[key]
  '''  isTar = False
    unvisited_set = list() 
    current_set = list()
    for key in graph:
        unvisited_set.append(key)
'''

