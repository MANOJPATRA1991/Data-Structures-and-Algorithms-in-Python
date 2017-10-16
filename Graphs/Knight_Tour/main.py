from Graphs.Graph.main import Graph


def knightGraph(bdSize):
    """
    If board is n x n, then bdSize = n
    Build a full graph for an n-by-n board
    Args:
        bdSize(int): number of rows in the board
    """
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            # converts this location on the board in terms
            # of row and column into a linear vertex number
            nodeId = posToNodeId(row, col, bdSize)
            # creates a list of legal moves for this position 
            # on the board
            newPositions = genLegalMoves(row, col, bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph


def posToNodeId(row, column, board_size):
    """
    Converts a location on the board in terms of row and column
    into a linear vertex number.
    The numbering starts at 0 and ends at (n-1).
    Args:
        row(int): The row number
        column(int): The column number
        board_size(int): The size of the board(n if nXn)
    """
    return row * board_size + column


def genLegalMoves(x, y, bdSize):
    """
    Creates a list of legal moves for this position
    on the board
    Args:
        x(int): Row number
        y(int): Column number
        bdSize(int): board size(n if nXn)
    """
    # store tuples of legal (x, y) coordinates 
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
    """
    Check for a legal coordinate, i.e., if
    the row or column number is positive and
    less than bdSize
    Args:
        x(int): The x or y coordinate
        bdSize(int): The board size (n if nXn)
    """
    if 0 <= x < bdSize:
        return True
    else:
        return False


def knightTour(n, path, u, limit):
    """
    This is a recursive function.
    The search algorithm used is Depth-First-Search(DFS).
    A DFS creates a search tree by exploring one branch at a time
    ass deeply as possible.
    Args:
        n(int): the current depth in the search tree
        path(list): the list of vertices visited up to the point
        u(Vertex): the vertex in the graph we wish to explore
        limit(int): the number of nodes in the path
    Returns:
        Boolean: If a path with 64 vertices is found, return True.
        If all neighbours of a particular vertex have been explored, 
        and we have not reached our goal of 64 vertices, we have
        reached a dead end. In this case, return False.
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
    """
    Returns a list of Vertex objects with
    fewest available moves sorted in increasing order
    Args:
        n(Vertex): Find vertices in neighborhood
                of n
    """
    # list to store tuples of moves and 
    # respective Vertex
    resList = []
    for v in n.getConnections():
        if v.getColor() == "white":
            c = 0
            for w in v.getConnections():
                if w.getColor() == "white":
                    c = c + 1
            resList.append((c,v))
    # select the vertex to go next that has the fewest available moves
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]


gg = knightGraph(64)
path = []
knightTour(64, path, gg.getVertex(64), 64)
