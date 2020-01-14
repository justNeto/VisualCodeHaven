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
