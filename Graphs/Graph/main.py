from Graphs.Vertex.main import Vertex

class Graph:
    """
    Attributes:
        vertList(dict): A dictionary of the vertices in the graph
        numVertices(int): Number of vertices in the graoh
    """
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        """
        Add a vertex to the graph
        Args:
            key(int): The key of the Vertex object
        Returns:
            Vertex: The newly added vertex
        """
        self.numVertices = self.numVertices + 1     # increment numVertices
        newVertex = Vertex(key)     # create a Vertex object with passed key
        self.vertList[key] = newVertex      # add the new vertex to the vertList as value of the passed key of this Graph
        return newVertex        # return the new vertex

    def getVertex(self, n):
        """
        Get vertex from this Graph
        Args:
            n(int): The key to search for in the Graph
        Returns:
            Vertex: If key 'n' is in vertList, return vertList[n]; else return None
        """
        if n in self.vertList:      # if key 'n' is in vertList
            return self.vertList[n]     # return vertList[n]
        else:
            return None     # else return None

    def __contains__(self, item):
        """
        Returns True if item is in vertList
        Args:
            item(int): Key to search for in the vertList
        """
        return item in self.vertList

    def addEdge(self, f, t, cost=0):
        """
        Add edge between two vertices in the graph if they exist
        Args:
            f(int): First key in vertList
            t(int): Second key in vertList
            cost(int, optional): Weight of the edge that connects the two vertices
        """
        if f not in self.vertList:
            newVertex = self.addVertex(f)
        if t not in self.vertList:
            newVertex = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        """
        Returns the names of all the vertices in the graph
        """
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

# g = Graph()
# for i in range(6):
#     g.addVertex(i)
# print(g.vertList)
# g.addEdge(0, 1, 5)
# g.addEdge(0, 5, 2)
# g.addEdge(1, 2, 4)
# g.addEdge(2, 3, 9)
# g.addEdge(3, 4, 7)
# g.addEdge(3, 5, 3)
# g.addEdge(4, 0, 1)
# g.addEdge(5, 4, 8)
# g.addEdge(5, 2, 1)
# for v in g:
#     for w in v.getConnections():
#         print("( %s, %s )" % (v.getId(), w.getId()))

