class Vertex:
    """
    Class representing vertices of the graph
    Attributes:
        id(string): The id of the vertex
        connectedTo(dict): Dictionary to keep track of the vertices to which it is connected and the weight of each edge
        distance(int):
        color(str)
        predecessor(Vertex)
    """
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.distance = 0
        self.color = "white"
        self.predecessor = None

    def addNeighbor(self, nbr, weight=0):
        """
        Add a connection from this vertex to another
        Args:
            nbr(Vertex): The vertex to connect to
            weight(int, optional): The weight of the edge between the two vertices 
        """
        self.connectedTo[nbr] = weight

    def __str__(self):
        """
        Returns string representation of vertices connected to this vertex
        """
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        """
        Returns all of the vertices in the adjacency list
        Returns:
            list: List containing the keys of all the vertices in the adjacency list
        """
        return self.connectedTo.keys()

    def getId(self):
        """
        Returns the id of this vertex
        Returns:
            str: id of this vertex
        """
        return self.id

    def getWeight(self, nbr):
        """
        Returns the weight of the edge from this vertex to the vertex passed as parameter
        Args:
            nbr(Vertex): The neighboring vertex
        Returns:
            int: The weight of the edge from this vertex to nbr
        """
        return self.connectedTo[nbr]

    def setDistance(self, n):
        self.distance = n

    def getDistance(self):
        return self.distance

    def setColor(self,color):
        self.color = color

    def getColor(self):
        return self.color

    def setPredecessor(self, v):
        self.predecessor = v

    def getPredecessor(self):
        return self.predecessor
