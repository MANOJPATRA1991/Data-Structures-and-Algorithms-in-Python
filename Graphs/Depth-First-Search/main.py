from Graphs.Graph.main import Graph

class DFSGraph(Graph):
    """
    A derived class from Graph base class
    Args:
        time(int): To keep track of when a Vertex is discovered
                and when it is completely explored
    """
    #
    # Run time for dfs => O(V+E)
    #
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        """
        Starts the depth first search
        """
        # Run time => O(V) for both the loops
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPredecessor(-1)

        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsVisit(aVertex)

    def dfsVisit(self, startVertex):
        """
        Args:
            startVertex(Vertex): The starting node for DFS
        """
        # Run-time => O(E) for the for loop
        #
        # as the loop will execute a max of once for every edge
        #
        # Recursive call occurs only if color of vertex is white
        #
        # CONCLUSION:
        #     all the children of a particular node in the
        #     depth first tree have a later discovery time
        #     and an earlier finish time than their parent
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for v in startVertex.getConnections():
            if v.getColor() == 'white':
                v.setPredecessor(startVertex)
                self.dfsVisit(v)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)
