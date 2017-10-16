from Graphs.Graph.main import Graph


def knightGraph(bdSize):
    """
    If board is n x n, then bdSize = n
    """
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph


def posToNodeId(row, column, board_size):
    return row * board_size + column


def genLegalMoves(x, y, bdSize):
    newMoves = []
    moveOffSets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in moveOffSets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoordinates(newX, bdSize) and \
            legalCoordinates(newY, bdSize):
            newMoves.append((newX, newY))
    return newMoves


def legalCoordinates(x, bdSize):
    if 0 <= x < bdSize:
        return True
    else:
        return False


def knightTour(n, path, u, limit):
    """
    :param n: the current depth in the search tree
    :param path: the list of vertices visited up to the point
    :param u: the vertex in the graph we wish to explore
    :param limit: the number of nodes in the path
    :return:
    """
    u.setColor("gray")
    path.append(u)
    if n < limit:
        nbrList = orderByAvail(u)
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == "white":
                done = knightTour(n+1, path, nbrList[i], limit)
            i = i + 1
        if not done:
            path.pop()
            u.setColor("white")
    else:
        done = True
    print(done)
    return done


def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == "white":
            c = 0
            for w in v.getConnections():
                if w.getColor() == "white":
                    c = c + 1
            resList.append((c,v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]


gg = knightGraph(64)
path = []
knightTour(64, path, gg.getVertex(64), 64)