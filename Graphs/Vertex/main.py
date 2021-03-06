class Vertex:
    """
    Class representing vertices of the graph
    Attributes:
        id(int/ string): The id of the vertex
        connectedTo(dict): Dictionary to keep track of the vertices
                        to which it is connected and the weight of each edge
        distance(int): Distance from the starting vertex used in BFS
        color(str): Color of the Vertex that specifies unexplored,
                    partially explored or completely explored, used in 
                    BFS and DFS
        predecessor(Vertex): The predecessor of this Vertex, used in
                    BFS and DFS
        discovery(int): The time taken to discover a Vertex, used in DFS
        finish(int): The time taken to finish exploring a Vertex, used in DFS
    """

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.distance = 0
        self.color = "white"
        self.predecessor = None
        self.discovery = 0
        self.finish = 0

    def addNeighbor(self, nbr, weight=0):
        """
        Add a connection from this vertex to another
        Args:
            nbr(Vertex): The vertex to connect to
            weight(int, optional): The weight of the edge
                                between the two vertices
        """
        self.connectedTo[nbr] = weight
        
    def __str__(self):
        """
        Returns string representation of vertices connected to this vertex
        """
        return str(self.id) + ' connectedTo: ' + \
            str([x.id for x in self.connectedTo])
        
    def getConnections(self):
        """
        Returns all of the vertices in the adjacency list
        Returns:
            list: List containing the keys of all the
                vertices in the adjacency list
        """
        return self.connectedTo.keys()
    
    def getId(self):
        """
        Returns the id of this vertex
        Returns:
            int: id of this vertex
        """
        return self.id
    
    def getWeight(self, nbr):
        """
        Returns the weight of the edge from this
        vertex to the vertex passed as parameter
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
    
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def setPredecessor(self, v):
        self.predecessor = v

    def getPredecessor(self):
        return self.predecessor

    def setDiscovery(self, t):
        self.discovery = t

    def getDiscovery(self):
        return self.discovery    

    def setFinish(self, t):
        self.finish = t
        
    def getFinish(self):
        return self.finish
