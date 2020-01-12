class Vertex:

    def __init__(self, x_coor,y_coor, someVertex):
        self.location = [x_coor, y_coor]
        self.name = someVertex
        self.neighbors = []

    def add_neighbor(self, neighbor):
        if neighbor.name not in self.neighbors:
            self.neighbors.append(neighbor.name)
            neighbor.neighbors.append(self.name)
            self.neighbors = sorted(self.neighbors)
            neighbor.neighbors = sorted(neighbor.neighbors)
        else:
            return 'There is something wrong here'

    def getNeighbors(self):
        return self.neighbors

class 


def dijkstraAlgorithm(graph,start,goal):
    shst_dis = {}
    pred = {}
    unseenNodes = graph
    infy = 200000
    path = []
    for node in unseenNodes:
        shortest_dis[node] = infy
    shst_dis[start] = 0
 
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shst_dis[node] < shst_dis[minNode]:
                minNode = node
 
        for childNode, weight in graph[minNode].items():
            if weight + shst_dis[minNode] < shst_dis[childNode]:
                shst_dis[childNode] = weight + shst_dis[minNode]
                pred[childNode] = minNode
        unseenNodes.pop(minNode)
 
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = pred[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0,start)
    if shst_dis[goal] != infy:
        print('The shortest distance from ' + start + ' to ' + goal + ' is ' + str(shst_dis[goal]))
        print('And the path is ' + str(path))
